import streamlit as st
import smtplib

st.markdown("<h1 style='text-align: center; color: green;'>Contact Me</h1>", unsafe_allow_html=True)

with st.form(key="email_sending_form", clear_on_submit=True):
    st.subheader("Your email address:")
    user_email_id = st.text_input(label=" ", key="user_email_address", label_visibility="collapsed")

    st.subheader("Your message:")
    user_text_message = st.text_area(label=" ", key="user_message", label_visibility="collapsed")

    button_value = st.form_submit_button('Submit')

    if button_value:
        s = smtplib.SMTP("smtp.gmail.com", 587)
        
        s.ehlo()

        # start TLS for security
        s.starttls()
        
        s.login("average2108student@gmail.com", "xszf raex xnue acbq")
        
        user_message = user_email_id + "\n" + user_text_message

        msg = "\r\n".join(["From: average2108student@gmail.com", "To: sara.2007.fga@gmail.com", "Subject: Proposal", "", user_message])
        
        s.sendmail("average2108student@gmail.com", "sara.2007.fga@gmail.com", msg)
        
        s.quit()