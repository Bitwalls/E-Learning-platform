import streamlit as st
import streamlit_book as stb
from PIL import Image

st.set_page_config(
    page_title="Bitwalls",
    page_icon="🅱️",
)

# Streamlit book properties
stb.set_chapter_config(path="ecourse_streamlit",
                       toc=False,
                       button='top',
                       button_previous='◀',
                       button_next='▶',
                       button_refresh='🔄 ')

# Add a logo (optional) in the sidebar
logo = Image.open(r'logo.png')
st.sidebar.image(logo, width=200)
# Add two expanders to provide additional information about this e-tutorial and the app


with st.sidebar.expander("About Bitwalls"):
    st.write("""
        Bitwalls is a white hat service provider, 
        which provides a free spam detecting tool 
        which can be used to test your Emails. Same 
        time Bitwall is also providing you the feature 
        of learning about the upcoming social Engineering 
        method including spams.
     """)

with st.sidebar.expander("About this app"):
    st.write("""
        Bitwall Spam Detector’s main 
        approach is to detect the spam emails as well 
        as spread the awareness about social engineering 
        method such as spams. Bitwalls Application also 
        provide some interesting features like Security 
        Awareness quizzes which allows users who using 
        the bitwalls to improve your knowledge about the 
        information security and to get some fun too.
     """)

# Create a user feedback section to collect comments and ratings from users
with st.sidebar.form(key='columns_in_form',
                     clear_on_submit=True):
    rating = st.slider("Please rate the app", min_value=1, max_value=5, value=3,
                       help='Drag the slider to rate the app. This is a 1-5 rating scale where 5 is the highest rating')
    text = st.text_input(label='Please leave your feedback here')
    submitted = st.form_submit_button('Submit')
    if submitted:
        st.write('Thanks for your feedback!')
        st.markdown('Your Rating:')
        # st.markdown(rating)
        if rating == 1:
            st.markdown("⭐")
        elif rating == 2:
            st.markdown("⭐⭐")
        elif rating == 3:
            st.markdown("⭐⭐⭐")
        elif rating == 4:
            st.markdown("⭐⭐⭐⭐")
        else:
            st.markdown("⭐⭐⭐⭐⭐")

        st.markdown('Your Feedback:')
        st.markdown(text)

