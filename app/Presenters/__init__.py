# Models
from app.Models.Users.user import User


class Presenter(User):
    def instanceView(self, view):
        return view(self.data)
