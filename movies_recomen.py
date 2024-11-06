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

# Initialize session state for storing conversation history
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Streamlit UI for chatbot interaction
user_input = st.text_input("You:", placeholder="Describe your movie preferences here...", label_visibility="collapsed")

# If the user provides input, fetch a recommendation and update conversation history
if user_input:
    response = get_movie_recommendation(user_input)
    
    # Append the user's message and the bot's response to the conversation history
    st.session_state.conversation.append(('You', user_input))
    st.session_state.conversation.append(('Chatbot', response))

    # Clear the input box after submission
    st.text_input("You:", value="", placeholder="Describe your movie preferences here...")

# Display conversation history
for speaker, message in st.session_state.conversation:
    if speaker == 'You':
        st.markdown(f'<div style="background-color:#F0F2F6; padding: 10px; border-radius: 10px; margin-bottom: 10px;">'
                    f'<b>You:</b> {message}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="background-color:#FEB47B; padding: 10px; border-radius: 10px; margin-bottom: 10px;">'
                    f'<b>Chatbot:</b> {message}</div>', unsafe_allow_html=True)

# Style adjustments for better UI
st.markdown("""
<style>
    /* Overall page style */
    body {
        background: #F8F9FA;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Title Styling */
    h1 {
        font-size: 36px;
        font-weight: bold;
        color: #333333;
        text-align: center;
        margin-top: 20px;
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

    /* Message Styling */
    .chat-message {
        display: flex;
        flex-direction: column;
        margin-bottom: 15px;
    }

    /* User's message bubble */
    .user-message {
        background-color: #F0F2F6;
        padding: 10px;
        border-radius: 10px;
        align-self: flex-start;
        margin-left: 5%;
        margin-bottom: 10px;
        width: auto;
        max-width: 80%;
    }

    /* Chatbot's message bubble */
    .chatbot-message {
        background-color: #FEB47B;
        padding: 10px;
        border-radius: 10px;
        align-self: flex-end;
        margin-right: 5%;
        margin-bottom: 10px;
        width: auto;
        max-width: 80%;
    }

    /* Styling for the chatbot's input box */
    input[type="text"] {
        font-size: 16px;
        padding: 12px;
        background-color: #fff;
        border-radius: 8px;
        border: 1px solid #ddd;
        width: 80%;
    }

    /* Fixed Input Box at bottom */
    .css-1i6f3iy {
        position: fixed;
        bottom: 10px;
        width: 80%;
        left: 10%;
        z-index: 100;
    }

    /* Chat container - Smooth scroll */
    .streamlit-expanderHeader {
        font-size: 16px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Scroll down to bottom to keep the conversation in view
st.markdown('<script>window.scrollTo(0, document.body.scrollHeight);</script>', unsafe_allow_html=True)

# Option to clear chat
if st.button("Clear Chat"):
    st.session_state.conversation.clear()  # Clears the chat history
    st.experimental_rerun()  # Rerun the app to reset chat history







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
