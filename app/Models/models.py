# Controllers
from app.Controllers.UserCPFController.UserCPFController import UserCPFController

# Mongoengine
from mongoengine import *


class ListCpf(EmbeddedDocument):
    cpf = StringField(required=True, unique=True)


class Users(Document):
    username = StringField(required=True, unique=True)
    name = StringField(required=True)
    email = EmailField(required=True)
    password = StringField(required=True, min_length=3, max_length=5)
    my_cpfs = ListField(EmbeddedDocumentField(ListCpf))

    @staticmethod
    def getGeneratedRandomCpf(username, num_list_cpf):
        return UserCPFController.getGeneratedCpf(Users.objects(username=username), num_list_cpf)

    @staticmethod
    def getValidationCpf(cpf):
        return UserCPFController.validatingCpf(cpf)

    @staticmethod
    def getCpfSaved(id, cpf):
        return UserCPFController.savingCpf(Users.objects(id=id), ListCpf(cpf=cpf))
