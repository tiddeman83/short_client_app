from multiprocessing import AuthenticationError
from flask import Flask, flash, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, current_user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink
from flask_migrate import Migrate

import pymysql

pymysql.install_as_MySQLdb()

db = SQLAlchemy()
#csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    Bootstrap(app)
    # csrf.init_app(app)
    import_modules(app)
    migrate = Migrate(app, db)

    with app.app_context():
        db.create_all()

    return app


def import_modules(app):
    from . import views
    app.register_blueprint(views.views)

    from . import auth
    app.register_blueprint(auth.authenticate)
