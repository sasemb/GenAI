import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(
  page_title="From Selfie to Sketchie", 
  page_icon="🤩", 
  layout="centered", 
  initial_sidebar_state="collapsed"
  menu_items={
        'Get Help': 'https://github.com/sasemb',
        'Report a bug': "https://github.com/sasemb",
        'About': "# Cool app to transform your selfies into sketchies!"
    }
)
st.title('Transform into Your Inner Superhero!')
st.subheader("Transform Your beautiful images into Superheroes with superpowers")
