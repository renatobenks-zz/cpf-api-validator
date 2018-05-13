from app import *

from flask import abort

# Views representing
from .Views.GenerateRandomCpf.GenerateRandomView import GenerateRandomView
from .Views.ValidateCpf.ValidateCpfView import ValidateCpfView
from .Views.SaveNewCpf.SaveNewCpfView import SaveNewCpfView


@app.route('/api/v1/random-generate', methods=["POST"])
@auth.login_required
def generate():
    username = request.json.get('username')
    num_list_cpf = request.json.get('num_list_cpf')
    if username and isinstance(username, str) and num_list_cpf and isinstance(num_list_cpf, int):
        generated = GenerateRandomView.getDataGeneratedCpf(username, num_list_cpf)
        return generated.render()
    else:
        abort(400)


@app.route('/api/v1/cpf-validate', methods=["POST"])
@auth.login_required
def validate():
    cpf = request.json.get('cpf')
    if cpf and isinstance(cpf, str):
        validation_cpf = ValidateCpfView.getDataValidationCpf(cpf)
        return validation_cpf.render()
    else:
        abort(400)


@app.route('/api/v1/save-cpf', methods=["POST"])
@auth.login_required
def save():
    id = request.json.get('id')
    cpf = request.json.get('cpf')
    if id and cpf and isinstance(id, str) and isinstance(cpf, str):
        cpf_saved = SaveNewCpfView.saveDataCpfReceived(id, cpf)
        return cpf_saved.render()
    else:
        abort(400)
