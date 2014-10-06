from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from blueprints.ga_arrows.web import ga_arrows

app = Flask(__name__)
app.register_blueprint(ga_arrows, url_prefix = '/ga_arrows')
Bootstrap(app)
# uncomment to serve CSS locally
#BOOTSTRAP_SERVE_LOCAL = True
app.config.from_object(__name__)



"""
@app.route("/")
def hello():
    return "Hello World!"
"""
@app.route("/")
def tool():
    return render_template('tool.html')

@app.route('/arcs')
def arcs():
    return render_template('arcs.html')

@app.route('/arrows')
def arrows():
    return render_template('arrows.html')


if __name__ == "__main__":
    app.run()