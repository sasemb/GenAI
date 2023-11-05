import streamlit as st
import io
import warnings

from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from streamlit_image_comparison import image_comparison

# Set up our connection to the API.
stability_api = client.StabilityInference(
    key=st.secrets["ai_key"],
    verbose=True, 
    engine="stable-diffusion-xl-1024-v1-0",
)

st.set_page_config(page_title="Sketches", page_icon=":)", layout="centered", initial_sidebar_state="collapsed")

st.title("It's time for transformation.")
image = st.file_uploader("Upload your image", type=['png', 'jpeg', 'jpg'])

st.text("Got no picture? Don't worry , Strike a pose and let's selfie")

image = st.camera_input("Take a picture")

if image is not None:
    # Open the image using Pillow
    img1 = Image.open(image)
    # Get the width and height of the image
    # width, height = img.size
    # left = (width - 512) / 2
    # top = (height - 512) / 2
    # right = (width + 512) / 2
    # bottom = (height + 512) / 2
    # cropped_image = img.crop((left, top, right, bottom))
    img1 = img1.resize((256, 256))
    answers = stability_api.generate("Convert the uploaded image of a person into a realistic pencil drawing sketch with a strong emphasis on capturing the facial features accurately. Ensure that the sketch highlights the key facial elements such as the eyes, nose, mouth, and overall facial structure. Pay attention to shading and details to create a lifelike pencil sketch. Please provide a high-quality sketch with attention to fine lines, shading, and proportions. The output should maintain the likeness of the original photograph while simulating a hand-drawn pencil sketch effect. Use your artistic judgment to create a visually appealing sketch.",
    init_image=img1, 
    start_schedule=0.6, 
    seed=12345,
    steps=50,
    cfg_scale=7, 
    width=256,
    height=256, # Generation height, defaults to 512 if not included.
    sampler=generation.SAMPLER_K_DPMPP_2M 
)
   
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                img2 = Image.open(io.BytesIO(artifact.binary)) # Set our resulting initial image generation as 'img2' to avoid overwriting our previous 'img' generation.
                # st.image(img2, width=256)
                image_comparison(
                    img1=img1,
                    img2=img2,
                    label1="Original",
                    label2="Gen AI",
                    width=256,
                    starting_position=50,
                    show_labels=True,
                    make_responsive=True,
                    in_memory=True,
                )
