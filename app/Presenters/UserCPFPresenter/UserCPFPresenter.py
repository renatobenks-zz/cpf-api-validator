# Super Presenter
from app.Presenters import Presenter

# Model
from Models.models import Users


class UserCPFPresenter(Presenter):
    def getGeneratedCpf(self, username, num_list_cpf):
        self.data = Users.getGeneratedRandomCpf(username, num_list_cpf)

    def getValidationCpf(self, cpf):
        self.data = Users.getValidationCpf(cpf)

    def saveCpfReceived(self, id, cpf):
        self.data = Users.getCpfSaved(id, cpf)
