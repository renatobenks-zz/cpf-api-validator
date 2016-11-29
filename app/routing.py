from app import *

# Presenters representing
from .Views.generateRandomCPF.generateRandomView import generateRandomView

# Instance views
generateRandomView = generateRandomView.getGeneratedCpf()


@app.route('/api/v1/random-generate')
@auth.login_required
def generate():
    return generateRandomView.render()
