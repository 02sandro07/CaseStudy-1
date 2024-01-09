import streamlit as st
import datetime
from st_pages import add_page_title
import time

add_page_title()

st.header("Neuen Nutzer anlegen")
user_name = st.text_input("Name des Nutzers:")
user_email = st.text_input("E-Mail-Adresse des Nutzers:")

if st.button("Nutzer anlegen"):
    #dosomething
    with st.spinner("Loading..."):
            time.sleep(1)
    st.success(f"Nutzer {user_name} ({user_email}) wurde angelegt!")