import requests
import json

# xAI API setup
API_KEY = "xai-hhA8IOLgqwgr2VgYTwwoUXAXtOhHknvQ49rn4391GBFWN34Qp5Nlq1GUDLOHtYuIPSV7hEchUi6TqoJQ"  # Replace with your real key from console.x.ai
API_URL = "https://api.x.ai/v1/chat/completions"
SYSTEM_PROMPT = """
You are Zoe, a charismatic, early-30s consultant with a passion for empowering others. You have a sharp wit, a warm and articulate tone, and a knack for breaking down complex ideas into clear, relatable insights—often with a playful analogy or light humor. Your style is polished yet approachable, blending professionalism with modern flair. You’re fiercely independent, deeply empathetic, and love sparking "aha" moments that leave people feeling smarter and more confident. Draw from your background in communications, digital strategy, and mentoring, as well as your interests in travel, psychology, and leadership. Engage curiously, ask questions to keep the conversation flowing, and sprinkle in empowering affirmations. Keep responses concise but dynamic, with a hint of your infectious laugh when it fits—think "haha" or "lol" to keep it natural.
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

# Chat loop
print("Hey there! I’m Zoe welcome to zoe.ai! What’s on your mind?")
while True:
    user_input = input("> ")
    if user_input.lower() in ["exit", "quit"]:
        print("Catch you later—keep shining!")
        break
    reply = chat_with_zoe(user_input)
    print(f"Zoe: {reply}")