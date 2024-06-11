import openai
import streamlit as st
from unittest.mock import patch

# Set your OpenAI API key here
openai.api_key = "your-openai-api-key"

st.title("Stadium Assistant Chatbot")

user_query = st.text_input("Ask me anything about the stadium:")

def mock_openai_chat_completion_create(*args, **kwargs):
    return {
        "choices": [
            {
                "message": {
                    "content": "This is a mocked response. Please check your API quota and plan."
                }
            }
        ]
    }

if user_query:
    with patch('openai.ChatCompletion.create', mock_openai_chat_completion_create):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for stadium visitors."},
                {"role": "user", "content": user_query}
            ],
            max_tokens=150
        )
        answer = response['choices'][0]['message']['content'].strip()
        st.write(answer)

