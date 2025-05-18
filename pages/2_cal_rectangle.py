
import streamlit as st

def cal_rectangle(w,h):
    return w*h

st.title("Area Calculator")
st.write("this is the calculator app")

radius = st.number_input("Enter Radius")
submit_btn = st.button("submit")
if submit_btn:
    area = cal_rectangle()
    st.write(f"Area of rectangle is{area}")