# Super class
from app.Views import View

# Presenter
from app.Presenters.generateRandomCPF.generateRandomPresenter import generateRandomPresenter

# Instance view
generateRandomPresenter = generateRandomPresenter()


class generateRandomView(View):
    @staticmethod
    def getGeneratedCpf(username):
        generateRandomPresenter.get_username(username)
        return generateRandomPresenter.instanceView(generateRandomView)
