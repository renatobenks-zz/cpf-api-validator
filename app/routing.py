from app import *

from flask import abort

# Views representing
from .Views.generateRandomCPF.generateRandomView import generateRandomView
from .Views.validateCpfView.validateCpfView import validateCpfView


@app.route('/api/v1/random-generate', methods=["POST"])
@auth.login_required
def generate():
    if request.json.get('username') and request.json.get('username') is str():
        generated = generateRandomView.getDataGeneratedCpf(request.json.get('username'))
        return generated.render()
    else:
        abort(400)


@app.route('/api/v1/cpf-validate', methods=["POST"])
@auth.login_required
def validate():
    pass
