from flask import redirect, render_template, request, session, url_for
from flask.helpers import flash

from notphotobooth import app

@app.route('/send-mail', methods=['POST', 'GET'])
def sendMail():
    if request.method == 'POST':
        subject = request.form['subject']
        return redirect(f'mailto:notphotobooth@gmail.com?subject={subject}')

@app.route('/', methods=['POST', 'GET'])
def index():

    title = 'Главная'

    return render_template('pages/index.html', title=title)

@app.route('/portfolio', methods=['POST', 'GET'])
def portfolio():

    title = 'Портфолио'

    return render_template('pages/portfolio.html', title=title)