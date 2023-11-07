from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://mphojvpl:Pagl4f8PgrJNX0LEVhf7ymQtRdGBhkg9@trumpet.db.elephantsql.com/mphojvpl"
db = SQLAlchemy(app)
from application import routes