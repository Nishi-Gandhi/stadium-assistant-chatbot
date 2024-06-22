Stadium Assistant Chatbot
This is a Streamlit-based chatbot designed to assist visitors at a stadium by providing information about various facilities, services, and policies.

Overview
The Stadium Assistant Chatbot allows users to ask questions about different aspects of the stadium, such as parking, seating, food options, security, and more. It provides predefined responses to common queries and can also generate responses using a language model for more complex inquiries.

Features
Provides information about:
Parking
Seating
Food options
Ticketing
Security
Lost and found
And more
Supports both predefined responses and responses generated by a language model
Easy to deploy and customize
Prerequisites
Make sure you have the following installed:

Python 3.7+
pip
Installation
Clone this repository:

sh
Copy code
git clone https://github.com/Nishi-Gandhi/stadium-assistant-chatbot.git
cd stadium-assistant-chatbot
Create a virtual environment:

sh
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:
sh
Copy code
.\venv\Scripts\activate
On macOS and Linux:
sh
Copy code
source venv/bin/activate
Install the required packages:

sh
Copy code
pip install -r requirements.txt
Setting Up Llama3
Follow the steps mentioned here to download a local instance of Ollama.

Start your local instance of the LLM service using the Llama3 model. Refer to the specific documentation of the service for setup instructions. Example command to start the service:

sh
Copy code
ollama serve --model llama3
Running the Chatbot
Start the Streamlit application:

sh
Copy code
streamlit run app.py
Open your web browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).

Project Structure
bash
Copy code
.
├── app.py              # Main Streamlit application
└── requirements.txt    # Python dependencies
Contributing
Feel free to submit issues and pull requests. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the Northeastern University(assignment)

