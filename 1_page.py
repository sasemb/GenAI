import streamlit as st
import streamlit.components.v1 as components
from streamlit.source_util import _on_pages_changed, get_pages
from pathlib import Path

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
st.title('From Selfie to :rainbow[Soccer] Sketchie ')
st.subheader("Unleash Your Inner Football Star 🌟")
st.image('iker.png' , width=256)
stripe_js = """<script async
  src="https://js.stripe.com/v3/buy-button.js">
</script>
<stripe-buy-button
  buy-button-id="buy_btn_1O95l6AdZK0V316xOrbOXyPg"
  publishable-key="{}"
>
</stripe-buy-button>
""".format(st.secrets["publishable_key"])


components.html(html=stripe_js, height=300)
