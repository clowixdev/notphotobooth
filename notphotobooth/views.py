from flask import redirect, render_template, request, session, url_for
from flask.helpers import flash
import git
from time import sleep
from datetime import datetime

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


@app.route('/send-request', methods=['POST', 'GET'])
def sendRequest():
    if request.method == 'POST':
        user_request = request.form['userRequest']
        username = request.form['username']
        phone = request.form['phone']
        email = request.form['email']
        with open('all_requests.txt', 'a') as f:
            data = 'application:\n\ttime: {}\n\tusername: {}\n\tphone: {}\n\tuser-request: {}\n\temail: {}\n'.format(
                str(datetime.utcnow()), username, phone, user_request, email)
            f.write(data)
        return redirect(url_for('index'))
