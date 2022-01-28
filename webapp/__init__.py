from flask import Flask, flash, render_template, redirect, url_for
from flask_login import LoginManager, current_user, login_required
from flask_migrate import Migrate


from webapp.db import db
from webapp.admin.views import blueprint as admin_blueprint
from webapp.article.views import blueprint as article_blueprint
from webapp.article.models import Article
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(article_blueprint)
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    @app.route('/')
    def index():
        print(url_for('index'))
        return render_template('index.html')

    @app.route('/gallery')
    def gallery():
        print(url_for('gallery'))
        return render_template('gallery.html')


    @app.route('/about')
    def about():
        print(url_for('about'))
        return render_template('about.html')

    return app
