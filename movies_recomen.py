import streamlit as st  # Import Streamlit library for web app development
import os  # Import os module to access environment variables
from groq import Groq  # Import Groq for interacting with the Groq API

# Set up Groq API client
key = os.getenv("GROQ_API")  # Get the Groq API key from environment variables
client = Groq(api_key=key)  # Create a Groq client with the API key

# Chat function
def chat(message):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message},
            ],
            model="llama3-8b-8192",
            temperature=0.7,
            max_tokens=5000,
            top_p=1,
            stop=None,
            stream=False,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return "Sorry, something went wrong: " + str(e)

# Movie recommendation function (mock-up for integration)
def recommend_movie(genre):
    # Dummy movie recommendations based on genre (you can replace this with real logic)
    recommendations = {
        "Action": ["Die Hard", "Mad Max", "John Wick"],
        "Comedy": ["The Hangover", "Superbad", "Step Brothers"],
        "Drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather"],
    }
    return recommendations.get(genre, ["No recommendations available for this genre."])

# Streamlit UI
st.title("🎬 Movie Recommendation Chatbot")  # Set the app title

# Theme selection
theme = st.selectbox(
    "Select Theme:",
    ["Default", "Gradient", "Solid Color", "Background Image"]
)

# Set CSS based on selected theme
if theme == "Gradient":
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, rgb(114, 194, 224), rgb(161, 196, 253));
            height: 100vh;
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
            height: 100vh;
            color: black;
        }
        </style>
        """, unsafe_allow_html=True)
elif theme == "Background Image":
    st.markdown(
        """
        <style>
        .stApp {
            # background-image: url('https://raw.githubusercontent.com/abdullahzunorain/chatbot/main/ai-technology-brain-background-digital-transformation-concept.jpg');
            background-image: url('https://raw.githubusercontent.com/abdullahzunorain/voice-to-voice-Chatbot/refs/heads/main/cartoon-ai-robot-character-scene.jpg');
            background-size: cover;
            background-position: center;
            height: 100vh;
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
            height: 100vh;
            color: black;
        }
        </style>
        """, unsafe_allow_html=True)

# Chat history initialization
if 'history' not in st.session_state:
    st.session_state.history = []

# Custom CSS for chat layout
st.markdown(
    """
    <style>
    .chat-container {
        max-height: 70vh;
        overflow-y: auto;
        margin-top: 10px;
    }
    .user-message {
        background-color: #E1FFC7;
        text-align: right;
        padding: 10px;
        border-radius: 15px;
        margin: 10px 0 10px 10px;
        display: inline-block;
        max-width: 90%;
        float: right;
        color: black;
    }
    .bot-message {
        background-color: #D1E7FF;
        text-align: left;
        padding: 10px;
        border-radius: 15px;
        margin: 10px 10px 10px 0;
        display: inline-block;
        max-width: 90%;
        float: left;
        color: black;
    }
    .clearfix::after {
        content: "";
        clear: both;
        display: table;
    }
    </style>
    """, unsafe_allow_html=True)

# Movie recommendation UI
genre_input = st.text_input("Enter a genre to get movie recommendations:")

if genre_input:
    recommendations = recommend_movie(genre_input)
    st.write("Recommended Movies:")
    for movie in recommendations:
        st.write(movie)

# Create a form for user input (chatbot)
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="Type your message here...", label_visibility="collapsed")
    submit_button = st.form_submit_button("Send")

# Handle chat interaction
if submit_button and user_input:
    with st.spinner("Linguist AI is typing..."):
        response = chat(user_input)
        st.session_state.history.append({"user": user_input, "bot": response})

# Display chat history
with st.container():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for chat in st.session_state.history:
        st.markdown(
            f"<div class='clearfix'><div class='user-message'>{chat['user']}</div></div>",
            unsafe_allow_html=True)
        st.markdown(
            f"<div class='clearfix'><div class='bot-message'>{chat['bot']}</div></div>",
            unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Position the input field and submit button at the bottom
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
    .stFormSubmitButton {
        position: fixed;
        bottom: 30px;
        left: 100%;
        transform: translateX(-50%);
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
