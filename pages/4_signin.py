import streamlit as st
import boto3
import hashlib
import hmac
import time
import base64
from st_pages import Page, show_pages, hide_pages
from captcha.image import ImageCaptcha
import random, string

#captcha values
length_captcha = 4
width = 100
height = 80


st.set_page_config(page_title="Pixar Star", page_icon="⭐", layout="centered", initial_sidebar_state="collapsed")

# Initialize the Cognito client
client = boto3.client('cognito-idp', region_name=st.secrets.region_name)

# Create a Streamlit sign-up form
st.title("Sign In")
email = st.text_input("Email").lower()
password = st.text_input("Password", type="password")
col1, col2 = st.columns(2)
if 'Captcha' not in st.session_state:
   st.session_state['Captcha'] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length_captcha))
print("the captcha is: ", st.session_state['Captcha'])
image = ImageCaptcha(width=width, height=height)
data = image.generate(st.session_state['Captcha'])
col1.image(data)
capta2_text = col2.text_area('Enter captcha text', height=30)
capta2_text= capta2_text.replace(" ", "")
if st.session_state['Captcha'].lower() == capta2_text.lower().strip():
    st.write("Captcha verified")
    submit_button = st.button("Sign In")
    if submit_button:
      message = email + st.secrets.APP_CLIENT_ID
      key = st.secrets.APP_CLIENT_SECRET.encode('utf-8')
      msg = message.encode('utf-8')
      secret_hash = base64.b64encode(hmac.new(key, msg, digestmod=hashlib.sha256).digest()).decode()
      try:
        response = client.initiate_auth(
            ClientId=st.secrets.APP_CLIENT_ID,
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': email,
                'PASSWORD': password,
                'SECRET_HASH': secret_hash
            }
        )
        st.success("User authenticated successfully! Start creating in the left menu.")
        # Extract the access token and refresh token from the response
        access_token = response['AuthenticationResult']['AccessToken']
        refresh_token = response['AuthenticationResult']['RefreshToken']
        st.session_state['token'] = access_token
      except client.exceptions.NotAuthorizedException:
        st.error("Incorrect user or password. Do you need to sign up?")
      except Exception as e:
        st.error("An error occurred during authentication.")
        st.error(str(e))
st.markdown(f"""Not a member?
    <a href="{st.secrets.APP_URI}/Sign%20Up" target = "_self"> 
        Sign Up
    </a>
""", unsafe_allow_html=True)


