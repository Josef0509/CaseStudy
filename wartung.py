import streamlit as st
from st_pages import add_page_title

add_page_title()

# Wartungsinformationen anzeigen
st.header("Wartungsinformationen")
if st.button("Wartungsinformationen anzeigen"):
    #dosomething
    st.success("Wartungsinformationen wurden angezeigt!")