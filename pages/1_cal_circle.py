import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Area Calculator", page_icon=":guardsman:", layout="wide")

def cal_circle(r):
    return math.pi * r * r

st.title("Area Circle Comparison Calculator")
st.write("This is the calculator app")

# Vertical Slide bars for radius (up-down)
radius1 = st.sidebar.slider("Adjust Radius of Circle 1", min_value=0.0, max_value=100.0, value=10.0, step=0.1)
radius2 = st.sidebar.slider("Adjust Radius of Circle 2", min_value=0.0, max_value=100.0, value=20.0, step=0.1)

# Calculate areas
area1 = cal_circle(radius1)
area2 = cal_circle(radius2)

st.write(f"Area of Circle 1 is: {area1:.2f}")
st.write(f"Area of Circle 2 is: {area2:.2f}")

# Dynamic Colors based on Radius
color1 = "#4CAF50" if radius1 <= 33 else ("#FFC107" if radius1 <= 66 else "#F44336")
color2 = "#4CAF50" if radius2 <= 33 else ("#FFC107" if radius2 <= 66 else "#F44336")

# Plotting the circles in real-time
fig, ax = plt.subplots(figsize=(6, 6))  # Adjusted size for two circles
ax.set_aspect('equal')
theta = np.linspace(0, 2 * np.pi, 100)

# Circle 1
x1 = radius1 * np.cos(theta)
y1 = radius1 * np.sin(theta)
ax.plot(x1, y1, color='black')
ax.fill(x1, y1, color=color1, alpha=0.6, label=f"Circle 1: Radius {radius1}")

# Circle 2
x2 = radius2 * np.cos(theta)
y2 = radius2 * np.sin(theta)
ax.plot(x2, y2, color='black')
ax.fill(x2, y2, color=color2, alpha=0.6, label=f"Circle 2: Radius {radius2}")

ax.legend()
ax.set_title("Circle Comparison")

st.pyplot(fig)
