import os


class Config:
    def __init__(self):
        pass

    APP_PATH = os.path.abspath(os.path.dirname(__file__) + '/..')

    @staticmethod
    def database():
        return {
            'adapter': 'Mysql',
            'host': 'localhost',
            'username': 'root',
            'password': '',
            'dbname': '',
            'charset': ''
        }

    @staticmethod
    def application():
        return {
            'appDir': Config.APP_PATH,
            'controllersDir': Config.APP_PATH + '/controllers/',
            'modelsDir': Config.APP_PATH + '/models/',
            'viewsDir': Config.APP_PATH + '/views/',
            'libraryDir': Config.APP_PATH + '/library/'
        }