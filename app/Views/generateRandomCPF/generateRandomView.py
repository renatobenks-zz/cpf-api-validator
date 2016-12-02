# Super view
from app.Views import View

# Presenter
from app.Presenters.generateRandomCPF.UserCPFPresenter import UserCPFPresenter

# Instance view
UserCPFPresenter = UserCPFPresenter()


class generateRandomView(View):
    @staticmethod
    def getDataGeneratedCpf(username):
        UserCPFPresenter.getGeneratedCpf(username)
        return UserCPFPresenter.instanceView(generateRandomView)
