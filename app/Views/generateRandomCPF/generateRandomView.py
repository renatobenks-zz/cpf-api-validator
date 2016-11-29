# Super class
from app.Views import View

# Presenter
from app.Presenters.generateRandomCPF.generateRandomPresenter import generateRandomPresenter

# Instance presenter
generateRandomPresenter = generateRandomPresenter()

class generateRandomView(View):
    @staticmethod
    def getGeneratedCpf():
        return generateRandomPresenter.instanceView(generateRandomView)
