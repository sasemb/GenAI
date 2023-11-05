import streamlit as st
import streamlit.components.v1 as components
from streamlit.source_util import _on_pages_changed, get_pages
#from st_pages import show_pages, Page, hide_pages
DEFAULT_PAGE = "1_page.py"
def get_all_pages():
    default_pages = get_pages(DEFAULT_PAGE)

    pages_path = Path("pages.json")

    if pages_path.exists():
        saved_default_pages = json.loads(pages_path.read_text())
    else:
        saved_default_pages = default_pages.copy()
        pages_path.write_text(json.dumps(default_pages, indent=4))

    return saved_default_pages


def clear_all_but_first_page():
    current_pages = get_pages(DEFAULT_PAGE)

    if len(current_pages.keys()) == 1:
        return

    get_all_pages()

    # Remove all but the first page
    key, val = list(current_pages.items())[0]
    current_pages.clear()
    current_pages[key] = val

    _on_pages_changed.send()
clear_all_but_first_page()
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
st.subheader("Discover which 'Friends' movie character you'll become🤩")
st.image('mp.jpg' , width=256)
stripe_js = """<script async
  src="https://js.stripe.com/v3/buy-button.js">
</script>
<stripe-buy-button
  buy-button-id="buy_btn_1O95l6AdZK0V316xOrbOXyPg"
  publishable-key="{}"
>
</stripe-buy-button>
""".format(st.secrets["publishable_key"])


#picture = st.camera_input("No need to fret if you don't already have a photo—snap a selfie right away!")
#if picture:
#    st.image(picture)
components.html(html=stripe_js, height=300)
