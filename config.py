import os
secret_key = os.urandom(22).hex()

class main(object):
    DEBUG = True
    TESTING = False

    SECRET_KEY = str(secret_key)

    LANGUAGES = ['en', 'ru']