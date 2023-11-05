import streamlit as st
import streamlit.components.v1 as components
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
st.subheader("Transform Your beautiful selfies to sketchies🤩")
st.image('mp.jpg' , width=256)
stripe_js = """<script async
  src="https://js.stripe.com/v3/buy-button.js">
</script>

<stripe-buy-button
  buy-button-id="buy_btn_1O6spGAWMFUrkCpQokDCuxQR"
  publishable-key="pk_live_51O8tBXAdZK0V316xuRGB4RGbQYKxoueByh4wfEo7S3AqFSpQQLDSBVZXlbhVvLNJ1jnr7N3DyXmZCl3CPYdXa6oV005ewXi72o"
>
</stripe-buy-button>
"""


#picture = st.camera_input("No need to fret if you don't already have a photo—snap a selfie right away!")
#if picture:
#    st.image(picture)
components.html(html=stripe_js, height=300)
