from flask import jsonify


class View(object):
    def __init__(self, data=""):
        self.data = {
            "data": data
        }

    def render(self):
        return jsonify(self.data)
