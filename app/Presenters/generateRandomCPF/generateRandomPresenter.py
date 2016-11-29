# Models
from app.Models.Users.user import User


class generateRandomPresenter(User):
    def __init__(self):
        self.changeUsername('Renatinho do gueto')

    def instanceView(self, view):
        return view(self.username)
