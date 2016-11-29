from server import app

# Modules
from app.Modules.Auth import *


@app.route('/api/names')
@auth.login_required
def getMusts():
    return jsonify(
        {
            'data': {
                'names': []
            }
        }
    )
