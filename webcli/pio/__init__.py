
from webcli.test import cmd
def init(app):
    app.register_blueprint(cmd.mapper)

