from flask import render_template, Blueprint

ga_arrows = Blueprint('ga_arrows', __name__, template_folder='templates', static_folder='static')

@ga_arrows.route('/tool')
def tool():
    return render_template('tool.html')
