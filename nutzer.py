import streamlit as st
import datetime
from st_pages import add_page_title

add_page_title()

st.header("Neuen Nutzer anlegen")
user_email = st.text_input("E-Mail-Adresse des Nutzers:")
user_name = st.text_input("Name des Nutzers:")
if st.button("Nutzer anlegen"):
    #dosomething
    st.success(f"Nutzer {user_name} ({user_email}) wurde angelegt!")