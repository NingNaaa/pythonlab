import streamlit as st

st.set_page_config(page_title='My Profile Page', page_icon='👤')

st.title("👤 My Profile Page")


# Profile Information
st.header("About Me")
name = st.text_input("Name:")
age = st.number_input("Age:", min_value=0, max_value=120, step=1)
bio = st.text_area("Short Bio:")

st.header("Contact Information")
email = st.text_input("Email:")
phone = st.text_input("Phone Number:")

# Display Profile Summary
st.subheader("Profile Summary")
if name and age and bio:
    st.write(f"**Name:** {name}")
    st.write(f"**Age:** {age}")
    st.write(f"**Bio:** {bio}")

if email:
    st.write(f"**Email:** {email}")

if phone:
    st.write(f"**Phone Number:** {phone}")

# Save Profile
if st.button("Save Profile"):
    st.success("Profile saved successfully!")
