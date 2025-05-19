import streamlit as st
from streamlit_chat import message
message("Hi")

user_input = st.text_input("Enter your message:")
if user_input:
    message(user_input, is_user=True)

