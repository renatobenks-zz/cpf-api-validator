# Super Presenter
from app.Presenters import Presenter


class generateRandomPresenter(Presenter):
    def __init__(self):
        self.data = {"username": self.username}

    def getGeneratedCpf(self, username):
        self.data = username
