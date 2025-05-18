import streamlit as st
st.set_page_config(page_title="Area Calculator", page_icon=":guardsman:", layout="wide")


import math
def cal_circle(r):
    return math.pi*r*r


st.title("Area CirCle Calculator")
st.write("this is the calculator app")

radius = st.number_input("Enter Radius")
submit_btn = st.button("submit")
if submit_btn:
    area = cal_circle(radius)
    st.write(f"Area of Circle is{area}")
