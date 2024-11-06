import os
import streamlit as st
from groq import Groq

# Configure Streamlit app settings (MUST be first)
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
            model="llama3-8b-8192",  # Adjust model if needed
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit UI for chatbot interaction
user_input = st.text_input("You:", placeholder="Describe your movie preferences here...", label_visibility="collapsed")

# If the user provides input, fetch a recommendation
if user_input:
    with st.spinner('Fetching movie recommendations...'):
        response = get_movie_recommendation(user_input)
    st.text_area("Chatbot:", value=response, height=200, max_chars=None, key="chatbot_response")

# Style adjustments for better UI
st.markdown("""
<style>
    /* Overall page style */
    body {
        background: linear-gradient(135deg, #ff7e5f, #feb47b);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Title Styling */
    h1 {
        font-size: 36px;
        font-weight: bold;
        color: white;
        text-align: center;
    }

    /* Input Box Styling */
    input {
        font-size: 16px;
        padding: 12px 20px;
        width: 100%;
        border: none;
        border-radius: 8px;
        margin-bottom: 20px;
        background-color: #ffffff;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    /* Text Area Styling */
    textarea {
        font-size: 16px;
        padding: 12px 20px;
        width: 100%;
        border-radius: 8px;
        background-color: #F0F2F6;
        color: #333333;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    /* Chatbot Button Styling */
    button {
        font-size: 16px;
        padding: 12px 24px;
        background-color: #FEB47B;
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    button:hover {
        background-color: #ff7e5f;
    }

    /* Floating Button Styling */
    .stButton>button {
        position: fixed;
        bottom: 20px;
        right: 20px;
        font-size: 16px;
        padding: 16px 24px;
        background-color: #ff7e5f;
        color: white;
        border-radius: 50%;
        border: none;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    .stButton>button:hover {
        background-color: #feb47b;
    }

    /* Adjusting Spinner Styling */
    .stSpinner {
        color: #ff7e5f;
        font-size: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Option to clear chat
if st.button("Clear Chat"):
    st.experimental_rerun()  # Clears the input and response







# # app.py

# import os
# import streamlit as st
# from groq import Groq

# # Configure Streamlit app settings
# st.set_page_config(page_title="Movie Recommendation Chatbot", layout="centered")

# # Title and intro
# st.title("🎬 Movie Recommendation Chatbot")
# st.write("Tell me about your favorite genres, actors, or movies you enjoyed, and I'll recommend something you'll like!")

# # API key setup: Retrieve the Groq API key from environment variables
# api_key = os.getenv("GROQ_API_KEY")
# if not api_key:
#     st.error("Error: API Key not found. Please set the GROQ_API_KEY environment variable.")
#     st.stop()

# # Initialize the Groq client
# client = Groq(api_key=api_key)

# # Function to get recommendations from Groq API
# def get_movie_recommendation(user_input):
#     try:
#         chat_completion = client.chat.completions.create(
#             messages=[
#                 {
#                     "role": "user",
#                     "content": f"I want a movie recommendation. {user_input}",
#                 }
#             ],
#             model="llama3-8b-8192",
#         )
#         return chat_completion.choices[0].message.content
#     except Exception as e:
#         return f"An error occurred: {e}"

# # Streamlit UI for chatbot interaction
# user_input = st.text_input("You:", placeholder="Describe your movie preferences here...")

# # If the user provides input, fetch a recommendation
# if user_input:
#     response = get_movie_recommendation(user_input)
#     st.text_area("Chatbot:", value=response, height=200, max_chars=None)

# # Style adjustments
# st.markdown("""
# <style>
# input {font-size: 16px;}
# textarea {font-size: 16px; background-color: #F0F2F6; color: #333333;}
# </style>
# """, unsafe_allow_html=True)
