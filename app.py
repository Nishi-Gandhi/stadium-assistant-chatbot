import streamlit as st
# from transformers import pipeline, set_seed
import json
import ollama



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
        if not predefined_response:
            answer = predefined_response
        else:
            try:
                # print('here')
                m = input('Which model do you want to use?\n\n 1. llama3 \n 2. Gemma:2B\n')
                if m=='1':             
                    # response =  llama3_model(user_query, max_length=150, num_return_sequences=1)[0]['generated_text'].strip()
                    response = ollama.chat('llama3', messages = [
                        {'role':'user',
                        'content': user_query}
                    ])
                    response = response['message']['content']
                elif m=='2':
                    # response = bert_model(user_query, max_length = 150, num_return_sequences = 1)[0]['generated_text'].strip()
                    response = ollama.chat('gemma:2b', messages = [
                        {'role':'user',
                        'content': user_query}
                    ])
                    response = response['message']['content']
                else:
                    raise(ValueError('Model not found!'))
                
                # answer = filter_response(response, user_query)
                answer = response
            except Exception as e:
                answer = "An error occurred: {}".format(e)

    st.write(answer)

