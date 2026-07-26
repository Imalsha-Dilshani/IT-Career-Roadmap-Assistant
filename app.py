import streamlit as st
from services.llm import generate_response
from services.router import classify_intent

st.title("IT Career Roadmap Assistant")

career = st.selectbox(
    "Target Career",
    ["AI Engineer", "Backend Developer", "DevOps Engineer", "Frontend Developer",]
)

skills = st.text_area("Current Skills")

if st.button("Generate Roadmap"):
    st.spinner("Generating...")