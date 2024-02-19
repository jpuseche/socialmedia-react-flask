from flask import Flask

def createApp():
    app = Flask(__name__)

    from .actions.post import post
    app.register_blueprint(post, url_prefix='/')

    return app