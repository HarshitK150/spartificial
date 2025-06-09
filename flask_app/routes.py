# Author: Harshit Kandpal <hkandpal944@gmail.com>
from flask import current_app as app, send_from_directory, jsonify
from flask import render_template, redirect, request, session, url_for, copy_current_request_context
from .utils.database.database  import database
from werkzeug.datastructures   import ImmutableMultiDict
from pprint import pprint
import json
import random
import functools
db = database()

from .chatbot import get_response

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = get_response(user_input)
    return jsonify({"response": response})
