# Author: Harshit Kandpal <hkandpal944@gmail.com>

#--------------------------------------------------
# Import Requirements
#--------------------------------------------------
import os
from flask import Flask
from flask_failsafe import failsafe
from dotenv import load_dotenv

#--------------------------------------------------
# Create a Failsafe Web Application
#--------------------------------------------------
@failsafe
def create_app(debug=True):
	load_dotenv()

	app = Flask(__name__)

	# This will prevent issues with cached static files
	app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
	app.debug = debug
	# The secret key is used to cryptographically-sign the cookies used for storing the session data.
	app.secret_key = 'AKWNF1231082fksejfOSEHFOISEHF24142124124124124iesfhsoijsopdjf'
	# ----------------------------------------------

	from .utils.database.database import database
	db = database()
	db.createTables(purge=True)

	# This will create two users
	db.createUser(email='owner@email.com' ,password='password', role='owner')
	db.createUser(email='guest@email.com' ,password='password', role='guest')
	# ----------------------------------------------

	from .routes import chat_routes
	app.register_blueprint(chat_routes)

	return app
