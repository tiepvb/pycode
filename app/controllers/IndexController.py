from core.Controller import Controller


class IndexController(Controller):

    def index(self):
        return self.setView()
