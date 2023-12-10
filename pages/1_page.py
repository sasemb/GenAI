# Import necessary libraries
import streamlit as st
import streamlit.components.v1 as components
from streamlit.source_util import _on_pages_changed, get_pages
from pathlib import Path

# Set page configuration options
st.set_page_config(
  page_title="From Selfie to Sketchie",  # Set the page title
  page_icon="🤩",  # Set a page icon
  layout="centered",  # Center the content on the page
  initial_sidebar_state="collapsed",  # Start with the sidebar collapsed
  menu_items={
        'Get Help': 'https://github.com/sasemb',  # Add a "Get Help" link to the menu
        'Report a bug': "https://github.com/sasemb",  # Add a "Report a bug" link to the menu
        'About': "# Cool app to transform your selfies into sketchies!"  # Add an "About" section to the menu
    }
)

# Set the main title of the application
st.title('From Selfie to :rainbow[Soccer] Sketchie ')

# Set a subheader for additional information
st.subheader("Unleash Your Inner Football Star 🌟")

# Display an image
st.image('iker.png' , width=256)

# Create HTML for a Stripe payment button
stripe_js = """<script async
  src="https://js.stripe.com/v3/buy-button.js">
</script>
<stripe-buy-button
  buy-button-id="buy_btn_1O95l6AdZK0V316xOrbOXyPg"
  publishable-key="{}"
>
</stripe-buy-button>
""".format(st.secrets["publishable_key"])

# Render the HTML with the Stripe payment button
components.html(html=stripe_js, height=300)
