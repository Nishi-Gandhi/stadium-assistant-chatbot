import streamlit as st
from transformers import pipeline, set_seed
import json

# Initialize the local DistilGPT-2 model
distilgpt2_model = pipeline('text-generation', model='distilgpt2')
set_seed(42)  # for reproducibility

st.title("Stadium Assistant Chatbot")

def is_simple_query(query):
    keywords = ["washroom", "restroom", "toilet", "bathroom"]
    return any(keyword in query.lower() for keyword in keywords)

def filter_response(response, query):
    keywords = ["washroom", "restroom", "toilet", "bathroom"]
    for keyword in keywords:
        if keyword in query.lower() and keyword in response.lower():
            return response
    return "I'm not sure where that is. Please check the stadium map."


def load_queries(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def generate_response(query):
    queries = load_queries('queries.json')
    for entry in queries:
        if entry['query'] in query.lower():
            return entry['response']
    return None


user_query = st.text_input("Ask me anything about the stadium:")

if user_query:
    if is_simple_query(user_query):
        answer = "The washrooms are located on the east and west ends of the stadium, near the main entrances."
    else:
        
        predefined_response = generate_response(user_query)
        if predefined_response:
            answer = predefined_response
        else:
            try:
                response = distilgpt2_model(user_query, max_length=150, num_return_sequences=1)[0]['generated_text'].strip()
                answer = filter_response(response, user_query)
            except Exception as e:
                answer = "An error occurred: {}".format(e)

    st.write(answer)

