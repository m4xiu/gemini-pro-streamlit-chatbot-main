import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Configure Streamlit page
st.set_page_config(
    page_title="Chat with Gemini!",
    page_icon=":brain:",
    layout="centered",
)

# Get API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=GOOGLE_API_KEY)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Title
st.title("🤖 Gemini AI ChatBot")

# Display chat history
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)

# User input
user_prompt = st.chat_input("Ask Gemini...")

if user_prompt:
    # Show user message
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append(("user", user_prompt))

    # Get response from Gemini
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_prompt
    )

    bot_reply = response.text

    # Show assistant response
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    st.session_state.chat_history.append(("assistant", bot_reply))
