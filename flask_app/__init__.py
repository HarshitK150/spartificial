# Author: Harshit Kandpal <hkandpal944@gmail.com>

#--------------------------------------------------
# Import Requirements
#--------------------------------------------------
import os
from flask import Flask
from flask_failsafe import failsafe
from dotenv import load_dotenv
from flask_session import Session
from redis import Redis

#--------------------------------------------------
# Create a Failsafe Web Application
#--------------------------------------------------
@failsafe
def create_app(debug=None):
	load_dotenv()

	if debug is None:
		debug = os.getenv("FLASK_DEBUG", "0") == "1"

	app = Flask(__name__)

	app.debug = debug

	if app.debug:
		# This will prevent issues with cached static files
		app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

	# The secret key is used to cryptographically-sign the cookies used for storing the session data.
	app.secret_key = os.getenv("APP_SECRET_KEY", "dev-only-secret")
	# ----------------------------------------------

	# Configure Redis-backed session
	app.config["SESSION_TYPE"] = "redis"
	app.config["SESSION_PERMANENT"] = False
	app.config["SESSION_USE_SIGNER"] = True
	app.config["SESSION_REDIS"] = Redis(host="redis", port=6379)  # Use "redis" if inside Docker network

	if not app.debug:
		app.config["SESSION_COOKIE_SECURE"] = True

	Session(app)

	from .utils.database.database import database
	db = database()
	db.createTables(purge=True)

	if app.debug:
		# This will create two users
		db.createUser(email='owner@email.com' ,password='password', role='owner')
		db.createUser(email='guest@email.com' ,password='password', role='guest')
		# ----------------------------------------------

	from .routes import chat_routes
	app.register_blueprint(chat_routes)

	return app
