import streamlit as st

st.title("IT Career Roadmap Assistant")

career = st.selectbox(
    "Target Career",
    ["AI Engineer", "Backend Developer", "DevOps Engineer"]
)

skills = st.text_area("Current Skills")

if st.button("Generate Roadmap"):
    st.spinner("Generating...")