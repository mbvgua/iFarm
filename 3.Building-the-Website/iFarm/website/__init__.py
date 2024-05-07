# import neccessary packages and modules
from flask import Flask, Blueprint
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from os import path


# instantiate the database and admin panel
db = SQLAlchemy()
db_name = 'database.db'
admin = Admin(name='iFarm Admin', template_mode='bootstrap3')
# bootstrap = Bootstrap5()


def create_app():
	""" function to create the application """

	# initialize your app
	app = Flask(__name__)
	###############################
	####make this more secure######
	####be an external file and####
	####import it as a module######
	###############################
	app.config['SECRET_KEY'] = 'TheNorthRemembers'
	app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
	# themes = 'cerulean', 'cosmo', 'cyborg', 'flatly', 'darkly'
	app.config['FLASK_ADMIN_SWATCH'] = 'flatly'

	# initialize the database and the admin panel
	db.init_app(app)
	admin.init_app(app)
	bootstrap = Bootstrap5(app)

	# import and register all the blueprints
	from .auth import auth
	app.register_blueprint(auth, url_prefix='/')

	from .views import views
	app.register_blueprint(views, url_prefix='/')

	from .models import User, Report
	create_database(app)


	# build and admin panel views
	admin.add_view(ModelView(User, db.session))
	admin.add_view(ModelView(Report, db.session))

	# implement login manager security
	login_manager = LoginManager()
	login_manager.init_app(app)
	login_manager.login_view = 'auth.login'		#what does this do?
	login_manager.login_message_category = 'warning'		#categorize login error message


	@login_manager.user_loader
	def load_user(id):
		""" function to automatically
		look up the db searchig if users primary is present
		"""
		return User.query.get(int(id))


	return app

def create_database(app):
	""" function to create the database"""
	with app.app_context():
		if not path.exists('website'+db_name):
			db.create_all()
			print('Created database succesfully!')
		else:
			print('An error occurred creating the database!')
