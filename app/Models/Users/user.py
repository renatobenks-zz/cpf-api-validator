# Controller
from app.Controllers.generateRandomController.generateRandomController import generateRandomController


class User(object):
    username = "Renato Benkendorf"

    @classmethod
    def changeUsername(cls, username):
        cls.username = generateRandomController.embaralhar_palavra(username)
