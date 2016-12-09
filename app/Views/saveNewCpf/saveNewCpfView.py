# Super view
from app.Views import View

# Presenter
from app.Presenters.UserCPFPresenter.UserCPFPresenter import UserCPFPresenter

# Instance presenter
UserCPFPresenter = UserCPFPresenter()


class SaveNewCpfView(View):
    @staticmethod
    def saveDataCpfReceived(id, cpf):
        pass
