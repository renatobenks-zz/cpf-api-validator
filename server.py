from flask import Flask

# initialization
app = Flask(__name__)

from app import *

if __name__ == '__main__':
    # db.drop_all()
    db.create_all()
    app.run(debug=True)
