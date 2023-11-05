import streamlit as st
import io
import warnings
import time

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

st.title("It's time for a change")

option = st.selectbox(
   "Upload a image or Selfie?",
   ("Upload", "Selfie"),
   index=None,
   
)
if option == "Upload":
    image = st.file_uploader("Upload your image", type=['png', 'jpeg', 'jpg'])
elif option == "Selfie":
    st.text("Got no picture? Don't worry , Strike a pose and let's selfie")
    image = st.camera_input("Take a picture")
time.sleep(15)
if image is not None:
    img1 = Image.open(image)
    img1 = img1.resize((256, 256))
    answers = stability_api.generate("Upload a real personality image, and use the Stable Diffusion Model to transform it into a highly detailed and realistic sketch. The sketch should capture the essence and character of the person in the uploaded image while maintaining a strong artistic quality. The final output should resemble a hand-drawn portrait with shading, texture, and fine details. Please prioritize creating a black and white sketch, but consider offering an option to adjust the level of stylization or introduce subtle color accents if desired. The output should be of the highest possible quality",
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
