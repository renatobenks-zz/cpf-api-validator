# Super Presenter
from app.Presenters import Presenter


class generateRandomPresenter(Presenter):
    def __init__(self):
        self.data = {"username": self.username}

    def get_username(self, username):
        self.data = username
