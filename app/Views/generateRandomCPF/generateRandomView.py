# Super class
from app.Views import View

# Presenter
from app.Presenters.generateRandomCPF.generateRandomPresenter import generateRandomPresenter

# Instance view
generateRandomPresenter = generateRandomPresenter()


class generateRandomView(View):
    @staticmethod
    def getDataGeneratedCpf(username):
        generateRandomPresenter.getGeneratedCpf(username)
        return generateRandomPresenter.instanceView(generateRandomView)
