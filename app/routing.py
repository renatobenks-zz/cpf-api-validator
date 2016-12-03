from app import *

from flask import abort

# Views representing
from .Views.generateRandomCpf.generateRandomView import generateRandomView
from .Views.validateCpf.validateCpfView import validateCpfView


@app.route('/api/v1/random-generate', methods=["POST"])
@auth.login_required
def generate():
    username = request.json.get('username')
    num_list_cpf = request.json.get('num_list_cpf')
    if username and isinstance(username, str) and num_list_cpf and isinstance(num_list_cpf, int):
        generated = generateRandomView.getDataGeneratedCpf(username, num_list_cpf)
        return generated.render()
    else:
        abort(400)


@app.route('/api/v1/cpf-validate', methods=["POST"])
@auth.login_required
def validate():
    if request.json.get('cpf') and isinstance(request.json.get('cpf'), str):
        validation_cpf = validateCpfView.getDataValidationCpf(request.json.get('cpf'))
        return validation_cpf.render()
    else:
        abort(400)


@app.route('/api/v1/save-cpf', methods=["POST"])
@auth.login_required
def save():
    id = request.json.get('id')
    cpf = request.json.get('cpf')
    if id and cpf and isinstance(id, str) and isinstance(cpf, str):
        pass
