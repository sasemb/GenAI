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
    key="sk-zEFlsT7SyKSnXH4JQL2QsKGZ5eZZcHTdClYUQ7XkVeKxrjb8",
    verbose=True, 
    engine="stable-diffusion-xl-1024-v1-0",
)

st.set_page_config(page_title="Sketches", page_icon=":)", layout="centered", initial_sidebar_state="collapsed")

st.title("Find out which football legend you'll transform into")

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
time.sleep(30)
if image is not None:
    img1 = Image.open(image)
    img1 = img1.resize((256, 256))
    answers = stability_api.generate("Convert given image into most resembling famous football players",
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
                    st.download_button(
                        label="Download the generated image",
                        data=artifact.binary,
                        file_name="result.jpg",
                        mime="image/png"
                    )
                   
