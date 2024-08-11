import streamlit as st
import smtplib

st.markdown("<h1 style='text-align: center; color: green;'>Contact Me</h1>", unsafe_allow_html=True)

st.subheader("Your email address:")
user_email_id = st.text_input(label=" ", key="user_email_address", label_visibility="collapsed")

st.subheader("Your message:")
user_text_message = st.text_area(label=" ", key="user_message", label_visibility="collapsed")