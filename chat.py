import google.generativeai as genai
import os

genai.configure(api_key='AIzaSyAjUy4Bn-TU3wHXT0O3m-GsQKDzaLjM8H4')

model = genai.GenerativeModel('gemini-pro')

messages = []

while True:
    message = input("Jayam: ")
    messages.append({
        "role": "user",
        "parts": ["give me 10 mcq on"+message+"give me an answer key after giving all the questions"],
    })

    response = model.generate_content(messages)

    messages.append({
        "role": "model",
        "parts": [response.text],
    })

    print("Gemini: " + response.text)
    # return response;
    