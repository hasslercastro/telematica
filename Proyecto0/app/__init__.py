from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_session import Session

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

app.config["SECRET_KEY"] = "kylXUOOV-PfbPIqeANnHAQ"

from app import views