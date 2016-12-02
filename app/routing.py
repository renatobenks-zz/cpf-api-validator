from app import *

from flask import abort

# Views representing
from .Views.generateRandomCPF.generateRandomView import generateRandomView
from .Views.validateCpfView.validateCpfView import validateCpfView


@app.route('/api/v1/random-generate', methods=["POST"])
@auth.login_required
def generate():
    if type(request.json.get('username')) == type(str()):
        generated = generateRandomView.getDataGeneratedCpf(request.json.get('username'))
        return generated.render()
    else:
        abort(500)


@app.route('/api/v1/cpf-validate', methods=["POST"])
@auth.login_required
def validate():
    pass
