import os
import streamlit as st
from groq import Groq

# Configure Streamlit app settings
st.set_page_config(page_title="Movie Recommendation Chatbot", layout="centered")

# Title and intro with styling
st.markdown("<h1 style='text-align: center; color: #FFB74D;'>🎬 Movie Recommendation Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px; color: #666;'>Tell me about your favorite genres, actors, or movies you enjoyed, and I'll recommend something you'll like!</p>", unsafe_allow_html=True)

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

# Store chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Streamlit UI for chatbot interaction
with st.container():
    # Display chat history container
    st.markdown("<div style='height: 400px; overflow-y: auto; border: 1px solid #ccc; padding: 10px; background-color: #FFFFFF; border-radius: 8px;'>", unsafe_allow_html=True)
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f"<div style='text-align: right; padding: 8px; background-color: #4A90E2; color: white; border-radius: 10px; margin: 5px 0; display: inline-block; max-width: 75%; float: right;'>{message['content']}</div><div style='clear: both;'></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='text-align: left; padding: 8px; background-color: #FFB74D; color: black; border-radius: 10px; margin: 5px 0; display: inline-block; max-width: 75%; float: left;'>{message['content']}</div><div style='clear: both;'></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Input area for user query
    user_input = st.text_input("You:", placeholder="Describe your movie preferences here...", label_visibility="collapsed")

    # If the user provides input, fetch a recommendation
    if user_input:
        response = get_movie_recommendation(user_input)
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        st.session_state.chat_history.append({"role": "bot", "content": response})

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
            background-image: url('https://raw.githubusercontent.com/abdullahzunorain/chatbot/main/ai-technology-brain-background-digital-transformation-concept.jpg');
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


# Add styling for input area and send button
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
            margin-top: 10px;
            border: none;
        }
        .stButton button:hover {
            background-color: #FF8C00;
        }
        div[data-testid="stTextInput"] label {
            font-size: 0;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Create a form for user movie preference input
with st.form(key='recommendation_form', clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="Type your favorite genre, actor, or movie here...", label_visibility="collapsed")
    submit_button = st.form_submit_button("Get Recommendation")

# Process the recommendation if input is provided
if submit_button and user_input:
    with st.spinner("CineMate is finding recommendations..."):
        # Mock function to get movie recommendations
        response = get_movie_recommendations(user_input)
        st.session_state.history.append({"user": user_input, "bot": response})

# Display recommendation history in a scrollable container
with st.container():
    st.markdown('<div class="recommendation-container">', unsafe_allow_html=True)
    for chat in st.session_state.history:
        st.markdown(
            f"<div class='clearfix'><div class='user-query'>{chat['user']}</div></div>",
            unsafe_allow_html=True)
        st.markdown(
            f"<div class='clearfix'><div class='bot-recommendation'>{chat['bot']}</div></div>",
            unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Position the input field statically at the bottom
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

# Position the submit button at the bottom center
st.markdown(
    """
    <style>
    .stFormSubmitButton {
        position: fixed;
        bottom: 30px;
        left: 100%;
        transform: translateX(-50%);
        z-index: 1;
    }
    </style>
    """, unsafe_allow_html=True)

def get_movie_recommendations(user_input):
    # Here you would typically have logic to generate recommendations
    # For now, we'll just return a placeholder response
    return f"Here are some recommended movies based on your interest in '{user_input}': Movie A, Movie B, and Movie C."





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
