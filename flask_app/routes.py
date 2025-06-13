# Author: Harshit Kandpal <hkandpal944@gmail.com>
import os
from flask import Blueprint, request, jsonify
from flask import render_template, redirect, request, session, url_for, copy_current_request_context
from .utils.database.database  import database
from openai import OpenAI

db = database()

chat_routes = Blueprint("chat_routes", __name__)

from .chatbot import get_response

@chat_routes.route("/")
def home():
    return render_template("index.html")

@chat_routes.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "Missing 'message' field"}), 400

    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-4.1-nano",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are Spartifical, a helpful campus/university assistant for Michigan State University."},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
