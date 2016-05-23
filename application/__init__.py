from flask import Flask
app = Flask(__name__)
app.template_folder = 'views'
app.config.from_object('config')
# =====
from flask.ext.sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
db = SQLAlchemy(app)
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionSQL = sessionmaker()
SessionSQL.configure(bind=engine)
# =====
if app.debug == True:
  from flask.ext.assets import Environment, Bundle
  assets = Environment(app)
  # assets.url = ; 
  # assets.directory = app.static_folder; 
  # assets.append_path('assets')
  scss = Bundle('../assets/scss/*.scss', filters='scss', output='css/scss-packed.css')
  assets.register('scss_all', scss)
  coffee = Bundle('../assets/coffee/*.coffee', filters='coffeescript', output='js/coffee-packed.js')
  assets.register('coffee_all', coffee)
# =====
from application import routes, models, controllers, views
# ипортируется модуль models, т.к. без него не работает корректно SQLAlchemy