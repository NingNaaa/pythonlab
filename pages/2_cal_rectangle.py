import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Area Calculator - Rectangle", page_icon=":guardsman:", layout="wide")

def cal_rectangle(w, h):
    return w * h

st.title("Area Calculator - Rectangle")
st.write("This is the calculator app")

# Rectangle Calculation
st.header("Rectangle Calculation")
width = st.number_input("Enter Width of Rectangle")
height = st.number_input("Enter Height of Rectangle")

if width > 0 and height > 0:
    area_rectangle = cal_rectangle(width, height)
    st.write(f"Area of Rectangle is: {area_rectangle:.2f}")

    # Display Rectangle
    fig, ax = plt.subplots()
    ax.plot([0, width, width, 0, 0], [0, 0, height, height, 0], color='green')
    ax.fill([0, width, width, 0, 0], [0, 0, height, height, 0], color='lightgreen', alpha=0.6)
    ax.set_aspect('equal')
    ax.set_title(f"Rectangle: {width} x {height}")

    st.pyplot(fig)
