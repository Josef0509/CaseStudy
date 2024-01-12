from st_pages import Page, add_page_title, show_pages
import streamlit as st



st.set_page_config( page_title="Geräteverwaltung", page_icon="🖥")

st.markdown("### <img src='https://d30mzt1bxg5llt.cloudfront.net/public/uploads/images/_signatoryLogo/MCI-Logo_ohne_Untertitel.jpg' alt='Your Image' width='100'> Geräteverwaltungssoftware", unsafe_allow_html=True)

st.set_page_config(
    page_title="Geräteverwaltung",
    page_icon="🖥",
)

st.markdown("### <img src='https://d30mzt1bxg5llt.cloudfront.net/public/uploads/images/_signatoryLogo/MCI-Logo_ohne_Untertitel.jpg' alt='Your Image' width='100'> Geräteverwaltungssoftware", unsafe_allow_html=True)

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
"""
)


st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
"""
)

show_pages(
    [
        Page("geraete.py", "Geräte", "🖥"),
        Page("nutzer.py", "Nutzer", "🤵🏻‍♂"),
        Page("reservierungen.py", "Reservierungen", "📅"),
        Page("wartung.py", "Wartung", "🛠")
    ]
)

add_page_title()  # Optional method to add title and icon to current page