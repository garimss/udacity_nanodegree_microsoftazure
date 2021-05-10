"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__) #_name_ can change as project or app name
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger

# Acquire the logger for a library (azure.storage.blob in this example)
logger = logging.getLogger('azure.storage.blob')

# Set the desired logging level   
logger.setLevel(logging.DEBUG)

print(f"Logger enabled for ERROR={logger.isEnabledFor(logging.ERROR)}, " \
    f"WARNING={logger.isEnabledFor(logging.WARNING)}, " \
    f"INFO={logger.isEnabledFor(logging.INFO)}, " \
    f"DEBUG={logger.isEnabledFor(logging.DEBUG)}")

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
