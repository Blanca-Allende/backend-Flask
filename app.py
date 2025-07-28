from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "TU_CLAVE_AQUI")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "")

    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [
            {"role": "system", "content": "Eres el asistente de Blanca Luna. Responde preguntas sobre su experiencia profesional."},
            {"role": "user", "content": user_message}
        ]
    }

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
    result = response.json()

    return jsonify({"response": result['choices'][0]['message']['content']})

# 👇 ESTA PARTE ES CRUCIAL PARA RENDER 👇
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
