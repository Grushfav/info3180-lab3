from flask import Flask
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
from .config import Config   

app = Flask(__name__)
app.config.from_object(Config)  # Load configuration

mail = Mail(app)                # Initialize Flask-Mail
csrf = CSRFProtect(app)         # Enable CSRF protection

from app import views           # Import views at the end
