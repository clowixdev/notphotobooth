from flask import Flask
from config import main

app = Flask(__name__, static_folder='static')
app.config.from_object(main)

from notphotobooth import views