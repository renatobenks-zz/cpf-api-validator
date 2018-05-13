# Super View
from app.Views import View

# Presenter
from app.Presenters.UserCPFPresenter.UserCPFPresenter import UserCPFPresenter

# Instance presenter
UserCPFPresenter = UserCPFPresenter()


class ValidateCpfView(View):
    @staticmethod
    def getDataValidationCpf(cpf):
        UserCPFPresenter.getValidationCpf(cpf)

        return UserCPFPresenter.instanceView(ValidateCpfView)
