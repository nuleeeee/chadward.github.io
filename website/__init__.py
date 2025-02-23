from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login	import LoginManager
import os

db = SQLAlchemy()
DB_NAME = "database.db"



def create_app():
	app = Flask(__name__)
	app.config["DEBUG"] = True
	app.config['SECRET_KEY'] = 'nols'
	app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
	# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:nols@localhost/flask'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

	db.init_app(app)
	migrate = Migrate(app, db)

	from .views import views
	from .auth import auth

	app.register_blueprint(views, url_prefix='/')
	app.register_blueprint(auth, url_prefix='/')

	from .models import User, Note

	create_database(app)

	login_manager = LoginManager()
	login_manager.login_view = 'auth.login'
	login_manager.init_app(app)

	@login_manager.user_loader
	def load_user(id):
		return User.query.get(int(id))

	return app

def create_database(app):
    if not os.path.exists('website/' + DB_NAME):  # Check if the database exists
        with app.app_context():  # Use app context
            db.create_all()  # Create all tables
        print("Database created!")
