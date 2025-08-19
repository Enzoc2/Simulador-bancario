from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['SECRET_KEY'] = 'vrbevnrelwkg'

    from .routes import routes 

    app.register_blueprint(routes, url_prefix='/')
    
    return app