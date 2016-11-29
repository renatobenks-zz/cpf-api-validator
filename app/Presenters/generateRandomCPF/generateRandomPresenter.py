# Models
from app.Models.Users.user import User


class generateRandomPresenter(User):
    def instanceView(self, view):
        return view(self.username)
