import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
st.set_page_config(
  page_title="From Selfie to Sketchie", 
  page_icon="🤩", 
  layout="centered", 
  initial_sidebar_state="collapsed",
  menu_items={
        'Get Help': 'https://github.com/sasemb',
        'Report a bug': "https://github.com/sasemb",
        'About': "# Cool app to transform your selfies into sketchies!"
    }
)
st.title('From Selfie to :rainbow[Sketchie] ')
st.subheader("Transform Your beautiful selfies to sketchies 🤩")
st.image('mp.jpg' , width=256)
picture = st.camera_input("No need to fret if you don't already have a photo—snap a selfie right away!")
if picture:
    st.image(picture)
