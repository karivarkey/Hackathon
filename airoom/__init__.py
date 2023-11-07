from flask import Flask
from airoom.login_route import login_bp

def create_app():
    app = Flask(__name__,template_folder='templates/')
    app.register_blueprint(login_bp)
    return app
