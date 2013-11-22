from flask import Flask
from flask_bootstrap import Bootstrap
from blueprints.ga_arrows.web import ga_arrows

app = Flask(__name__)
app.register_blueprint(ga_arrows, url_prefix = '/ga_arrows')
Bootstrap(app)
import pdb;pdb.set_trace()
BOOTSTRAP_SERVE_LOCAL = True
app.config.from_object(__name__)
#app.config.from_object({'BOOTSTRAP_SERVE_LOCAL' : True})


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()