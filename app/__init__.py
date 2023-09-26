from flask import Flask

def create_app():
    app = Flask(__name__)

    from .views import index
    app.register_blueprint(index.bp)

    return app
