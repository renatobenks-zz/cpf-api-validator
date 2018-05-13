class Presenter(object):
    def instanceView(self, view):
        return view(self.data)
