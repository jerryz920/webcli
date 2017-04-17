
from webcli.pio import cmd
def init(app):
    app.register_blueprint(cmd.mapper)

