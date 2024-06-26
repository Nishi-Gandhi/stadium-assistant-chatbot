# Stadium Assistant Chatbot

This is a Streamlit-based chatbot designed to assist visitors at a stadium by providing information about various facilities, services, and policies.

## Overview

The Stadium Assistant Chatbot allows users to ask questions about different aspects of the stadium, such as parking, seating, food options, security, and more. It provides predefined responses to common queries and can also generate responses using a language model for more complex inquiries.

## Features

- Provides information about:
  - Parking
  - Seating
  - Food options
  - Ticketing
  - Security
  - Lost and found
  - And more
- Supports both predefined responses and responses generated by a language model
- Easy to deploy and customize

## Prerequisites

Make sure you have the following installed:

- Python 3.7+
- pip

## Installation

1. Clone this repository:

   ```sh
   git clone https://github.com/Nishi-Gandhi/stadium-assistant-chatbot.git
   cd stadium-assistant-chatbot


2. Install the required packages:

   ```sh
   pip install -r requirements.txt

## Setting Up Llama3

Follow the steps mentioned [here](https://github.com/ollama/ollama?tab=readme-ov-file) to download a local instance of Ollama.

Start your local instance of the LLM service using the Llama3 model. Refer to the specific documentation of the service for setup instructions. 


## Running the Chatbot

Start the Streamlit application:

```sh
streamlit run app.py

## Open your web browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).

After entering query select model.

