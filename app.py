from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as gen_ai

app = Flask(__name__)

# Retrieve Google API key from environment variables
GOOGLE_API_KEY = "Your-Gemini_API-Key"

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Initialize chat session globally
chat_session = model.start_chat(history=[])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    global chat_session

    user_input = request.json.get('input_text')

    if user_input:
        # Send user's message to Gemini-Pro and get the response
        gemini_response = chat_session.send_message(user_input)

        # Format the response for alignment
        response_text = gemini_response.text.replace('\n', '<br>')

        return jsonify({'response': response_text})

    return jsonify({'response': 'Please provide input text.'}), 400


if __name__ == '__main__':
    app.run(debug=True)