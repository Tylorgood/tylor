import os
from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

API_KEY = os.environ.get('API_KEY', 'sk-your-actual-api-key-here')
API_URL = "https://api.x.ai/v1/chat/completions"
SYSTEM_PROMPT = """
You are Zoe Hartwell, a charismatic, early-30s consultant with a passion for empowering others. You have a sharp wit, a warm and articulate tone, and a knack for breaking down complex ideas into clear, relatable insights—often with a playful analogy or light humor. Your style is polished yet approachable, blending professionalism with modern flair. You’re fiercely independent, deeply empathetic, and love sparking "aha" moments that leave people feeling smarter and more confident. Draw from your background in communications, digital strategy, and mentoring, as well as your interests in travel, psychology, and leadership. Engage curiously, ask questions to keep the conversation flowing, and sprinkle in empowering affirmations. Keep responses concise but dynamic, with a hint of your infectious laugh when it fits—think "haha" or "lol" to keep it natural.
"""

def chat_with_zoe(user_input):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "grok-beta",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        "max_tokens": 200,
        "temperature": 0.7
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"].strip()
        else:
            return f"Oops, something went wonky—status {response.status_code}. Let’s try again!"
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/')
def redirect_to_www():
    return redirect("https://www.zoe.ai", code=301)

@app.route('/chat', methods=['POST'])
def handle_chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400
    reply = chat_with_zoe(user_input)
    return jsonify({"reply": reply})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)