import os
import streamlit as st
from groq import Groq

# Set up Streamlit app configuration
st.set_page_config(page_title="🎬 CineMate: Movie Recommendation Chatbot", layout="centered")

# Theme selection
theme = st.selectbox(
    "Select Theme:",
    ["Default", "Gradient", "Solid Color", "Background Image"]
)

# Title and introduction with improved styling
st.markdown("<h1 style='text-align: center; color: #FFB74D;'>🎬 CineMate: Your Movie Recommendation Bot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px; color: #666;'>Tell me about your favorite genres, actors, or movies, and I'll recommend something you'll love! 🍿</p>", unsafe_allow_html=True)

# Retrieve API key for Groq from environment variables
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("API Key not found! Please set the GROQ_API_KEY environment variable.")
    st.stop()

# Initialize the Groq client
client = Groq(api_key=api_key)

# Function to get movie recommendations using Groq API
def get_movie_recommendation(user_input):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": f"Recommend me a movie. {user_input}"}
            ],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred while fetching recommendations: {e}"

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Container for displaying chat history
with st.container():
    st.markdown("<div style='height: 400px; overflow-y: auto; border: 1px solid #ccc; padding: 10px; background-color: #F9F9F9; border-radius: 8px;'>", unsafe_allow_html=True)
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f"<div style='text-align: right; padding: 8px; background-color: #4A90E2; color: white; border-radius: 10px; margin: 5px 0; display: inline-block; max-width: 75%; float: right;'>{message['content']}</div><div style='clear: both;'></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='text-align: left; padding: 8px; background-color: #FFB74D; color: black; border-radius: 10px; margin: 5px 0; display: inline-block; max-width: 75%; float: left;'>{message['content']}</div><div style='clear: both;'></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Input area and submit button in a fixed position at the bottom
user_input = st.text_input("You:", placeholder="Describe your movie preferences here...")

# Process user input when submit button is clicked
if user_input:
    # Store user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # Get the response from Groq API
    response = get_movie_recommendation(user_input)
    
    # Store bot response
    st.session_state.chat_history.append({"role": "bot", "content": response})
    user_input = ""  # Clear input after submission


# Theme-based styling with CSS
if theme == "Gradient":
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, rgb(114, 194, 224), rgb(161, 196, 253));
            color: black;
        }
        </style>
        """, unsafe_allow_html=True)
elif theme == "Solid Color":
    st.markdown(
        """
        <style>
        .stApp {
            background-color: rgb(240, 240, 240);
            color: black;
        }
        </style>
        """, unsafe_allow_html=True)
elif theme == "Background Image":
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://raw.githubusercontent.com/abdullahzunorain/chatbot/main/ai-technology-brain-background-digital-transformation-concept.jpg');
            background-size: cover;
            background-position: center;
            color: black;
        }
        .stTitle {
            color: #FFFFFF !important;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
        }
        </style>
        """, unsafe_allow_html=True)
else:
    st.markdown(
        """
        <style>
        .stApp {
            background-color: rgb(255, 255, 255);
            color: black;
        }
        </style>
        """, unsafe_allow_html=True)

# Custom CSS for input field and button styling
st.markdown("""
    <style>
        input {
            font-size: 16px;
            padding: 10px;
            width: 100%;
            border-radius: 8px;
            border: 1px solid #ccc;
            background-color: #FFFFFF;
            color: #333;
        }
        .stButton button {
            font-size: 16px;
            background-color: #FFB74D;
            color: black;
            padding: 8px 16px;
            border-radius: 8px;
            border: none;
            margin-top: 10px;
        }
        .stButton button:hover {
            background-color: #FF8C00;
        }
    </style>
""", unsafe_allow_html=True)

# Function to mock recommendations (useful for testing without API calls)
def get_mock_recommendations(user_input):
    return f"Based on your interest in '{user_input}', here are some top picks: Movie A, Movie B, and Movie C."

# Display recommendation history in a scrollable container
with st.container():
    st.markdown('<div class="recommendation-container">', unsafe_allow_html=True)
    for chat in st.session_state.chat_history:
        if chat["role"] == "user":
            st.markdown(f"<div style='text-align: right; padding: 8px; color: white; background-color: #4A90E2; border-radius: 10px; margin: 5px 0; display: inline-block; max-width: 70%;'>{chat['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='text-align: left; padding: 8px; color: black; background-color: #FFB74D; border-radius: 10px; margin: 5px 0; display: inline-block; max-width: 70%;'>{chat['content']}</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Additional styling to position the input area at the bottom
st.markdown(
    """
    <style>
    .stTextInput {
        position: fixed;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        width: 60%;
        z-index: 1;
    }
    </style>
    """, unsafe_allow_html=True)






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
