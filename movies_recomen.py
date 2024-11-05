# app.py

import os
import streamlit as st
from groq import Groq

# Configure Streamlit app settings
st.set_page_config(page_title="Movie Recommendation Chatbot", layout="centered")

# Title and intro
st.title("🎬 Movie Recommendation Chatbot")
st.write("Tell me about your favorite genres, actors, or movies you enjoyed, and I'll recommend something you'll like!")

# API key setup: Retrieve the Groq API key from environment variables
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("Error: API Key not found. Please set the GROQ_API_KEY environment variable.")
    st.stop()

# Initialize the Groq client
client = Groq(api_key=api_key)

# Function to get recommendations from Groq API
def get_movie_recommendation(user_input):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"I want a movie recommendation. {user_input}",
                }
            ],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit UI for chatbot interaction
user_input = st.text_input("You:", placeholder="Describe your movie preferences here...")

# If the user provides input, fetch a recommendation
if user_input:
    response = get_movie_recommendation(user_input)
    st.text_area("Chatbot:", value=response, height=200, max_chars=None)

# Style adjustments
st.markdown("""
<style>
input {font-size: 16px;}
textarea {font-size: 16px; background-color: #F0F2F6; color: #333333;}
</style>
""", unsafe_allow_html=True)
