# Super View
from app.Views import View

# Presenter
from app.Presenters.UserCPFPresenter.UserCPFPresenter import UserCPFPresenter

# Instance presenter
UserCPFPresenter = UserCPFPresenter()


class validateCpfView(View):
    @staticmethod
    def getDataValidationCpf(cpf):
        UserCPFPresenter.getValidationCpf(cpf)

        return UserCPFPresenter.instanceView(validateCpfView)
