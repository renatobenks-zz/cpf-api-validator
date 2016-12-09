# Super view
from app.Views import View

# Presenter
from app.Presenters.UserCPFPresenter.UserCPFPresenter import UserCPFPresenter

# Instance presenter
UserCPFPresenter = UserCPFPresenter()


class GenerateRandomView(View):
    @staticmethod
    def getDataGeneratedCpf(username, num_list_cpf):
        UserCPFPresenter.getGeneratedCpf(username, num_list_cpf)

        return UserCPFPresenter.instanceView(GenerateRandomView)
