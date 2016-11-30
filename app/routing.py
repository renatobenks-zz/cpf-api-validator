from app import *

# Presenters representing
from .Views.generateRandomCPF.generateRandomView import generateRandomView


@app.route('/api/v1/random-generate', methods=["POST"])
@auth.login_required
def generate():
    generated = generateRandomView.getGeneratedCpf(request.json.get('username'))
    return generated.render()
