from flask import Flask
# from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# DB credentials
user, password = 'illyapetrusenko1', '0445450232aA'
host = 'https://illyapetrusenko1.mysql.pythonanywhere-services.com'
db = 'illyapetrusenko1$proshtor' # dbFlask was created as a PythonAnywhere MySQL database

# connection string: mysql://user:pword@host/db
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(user, password, host, db)
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models