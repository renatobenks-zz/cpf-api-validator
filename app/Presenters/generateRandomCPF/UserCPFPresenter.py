# Super Presenter
from app.Presenters import Presenter

# Model
from Models.models import Users


class UserCPFPresenter(Presenter):
    def getGeneratedCpf(self, username):
        self.data = Users.getGeneratedRandomCpf(username)
