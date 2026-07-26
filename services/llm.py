import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
 streamlit-site


 main
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    api_key = st.secrets["OPENROUTER_API_KEY"]

 streamlit-site

 main
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)


def generate_response(prompt):

    response = client.chat.completions.create(
        model="meta-llama/llama-3.3-70b-instruct",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content