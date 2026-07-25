import streamlit as st
from services.llm import generate_response

st.title("IT Career Roadmap Assistant")

career = st.selectbox(
    "Target Career",
    [
        "AI Engineer",
        "Backend Developer",
        "DevOps Engineer",
        "Frontend Developer",
        "Data Engineer",
        "Data Scientist",
        "Machine Learning Engineer",
        "Mobile App Developer",
        "Network Engineer",
        "Product Manager",
        "QA Engineer",
        "Security Engineer",
    ]
)

skills = st.text_area("Current Skills")


if st.button("Generate Roadmap"):

    with st.spinner("Generating..."):

        prompt = f"""
        You are an IT career roadmap assistant.

        Target Career:
        {career}

        Current Skills:
        {skills}

        Create a learning roadmap with:
        1. Missing skills
        2. Technologies to learn
        3. 3 month roadmap
        4. Projects to build
        """

        response = generate_response(prompt)

        st.subheader("Career Roadmap")
        st.write(response)