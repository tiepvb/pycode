from flask import Flask
from app.config.router import routes
from app.config.config import Config


def loader():
    temp = Config.application()
    app = Flask(__name__, template_folder=temp['viewsDir'])
    '''setup router'''
    routes(app)
    return app
