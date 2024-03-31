from django.shortcuts import render
import google.generativeai as genai
import os

from django.http import JsonResponse

# Configure generative AI
genai.configure(api_key='AIzaSyAjUy4Bn-TU3wHXT0O3m-GsQKDzaLjM8H4')
model = genai.GenerativeModel('gemini-pro')
messages = []  # Move messages outside the view function to retain state

def process_chat(request):
    if request.method == 'POST':
        chat = request.POST.get('chat')
        messages.append({
            "role": "user",
            "parts": [chat],  # Use the chat input from the form
        })

        response = model.generate_content(messages)

        messages.append({
            "role": "model",
            "parts": [response.text],
        })

        # Return the response text as JSON
        return JsonResponse({'response': response.text})
    else:
        return JsonResponse({'error': 'Invalid request method'})
