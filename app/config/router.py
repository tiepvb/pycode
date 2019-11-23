from core.Router import Router
from app.controllers import *


def routes(app):
    """
    default router root
    app, name, url, class controller, action, methods
    """
    Router(app, 'index', '/', IndexController, 'index', methods=['GET'])
