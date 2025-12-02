import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from prompts import get_art_gallery_prompt
from gallery_api import get_exhibition_info, get_artist_info
from dotenv import load_dotenv
import os
import logging

# -------------------------
# Load environment variables
# -------------------------
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
      st.error("No OpenAI API key found! Please add it to .env")
      st.stop()
os.environ["OPENAI_API_KEY"] = api_key

# -------------------------
# Setup logging
# -------------------------
logging.basicConfig(
    filename='chatbot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# -------------------------
# Streamlit UI
# -------------------------
st.title("🎨 Art Gallery Chatbot")
st.write("Ask questions about our art gallery, exhibitions, or artists!")

# Session state to keep chat history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("Your question:")

if user_input:
    try:
        # -------------------------
        # Get prompt template
        # -------------------------
        prompt_template = get_art_gallery_prompt()

        # -------------------------
        # Chat LLM setup
        # -------------------------
        llm = ChatOpenAI(temperature=0.5, model_name="gpt-3.5-turbo")
        chain = LLMChain(llm=llm, prompt=prompt_template)

        # -------------------------
        # Generate response
        # -------------------------
        response = chain.run({"question": user_input})

        # -------------------------
        # Display response
        # -------------------------
        st.write(response)

        # -------------------------
        # Store chat history
        # -------------------------
        st.session_state.history.append({"user": user_input, "bot": response})

        # -------------------------
        # Show chat history
        # -------------------------
        st.write("### Chat History")
        for chat in st.session_state.history:
            st.markdown(f"**You:** {chat['user']}")
            st.markdown(f"**Bot:** {chat['bot']}")

        # -------------------------
        # Logging
        # -------------------------
        logging.info(f"User asked: {user_input}")
        logging.info(f"Bot responded: {response}")

    except Exception as e:
        st.error(f"Oops, something went wrong: {e}")
        logging.error(f"Error: {e}")
