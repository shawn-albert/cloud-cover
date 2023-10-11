# app.py
import streamlit as st
from frontend.components import ChatHistory, TextInput
from backend.agents.chat_agent import ChatAgent

# Global Variables
chat_history = []  # List of tuples: (sender, message, is_code)
chat_agent = ChatAgent()

def main():
    """Main function to render the Streamlit app."""
    st.title("ChatGPT Interface")

    # Load custom styles
    st.markdown(open("frontend/styles/ChatHistory.css").read(), unsafe_allow_html=True)
    st.markdown(open("frontend/styles/TextInput.css").read(), unsafe_allow_html=True)

    # Render Components
    global chat_history
    ChatHistory.render_chat_history(chat_history)
    chat_history = TextInput.handle_text_input(chat_agent, chat_history)

    # Stop button
    if st.button("Stop Generating"):
        # Assuming chat_agent has a method to stop generating
        chat_agent.stop_generating()
        st.experimental_rerun()

# Run main function
if __name__ == "__main__":
    main()
