from flask import Flask, request, jsonify
import google.generativeai as genai

# Configure GenAI API key
genai.configure(api_key='AIzaSyAjUy4Bn-TU3wHXT0O3m-GsQKDzaLjM8H4')
model = genai.GenerativeModel('gemini-pro')

app = Flask(__name__)

@app.route('/generate_response', methods=['POST'])
def generate_response():
    # Extract the message from the request JSON
    request_data = request.get_json()
    message = request_data.get('message', '')

    # Generate a response using GenAI
    messages = [{
        "role": "user",
        "parts": ["give me 10 mcq on" + message + "give me an answer key after giving all the questions"],
    }]
    response = model.generate_content(messages)

    # Return the response as JSON
    return jsonify({'response': response.text})

if __name__ == '_main_':
    app.run(debug=True)