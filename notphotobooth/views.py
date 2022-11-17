from flask import redirect, render_template, request, session, url_for
from flask.helpers import flash

from notphotobooth import app

@app.route('/', methods=['POST', 'GET'])
def index():

    title = 'Главная'

    return render_template('pages/index.html', title=title)