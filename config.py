DEBUG = True

CSRF_ENABLED = True # активирует предотвращение поддельных межсайтовых запросов
CSRF_SESSION_KEY = "secret"
SECRET_KEY = 'you-will-never-guess' # криптографический токен при валидации формы

# БАЗЫ ДАННЫХ
import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# SQLALCHEMY_DATABASE_URI необходим для расширения Flask-SQLAlchemy. 
# Это путь к файлу с нашей базой данных. app.db - название базы данных.
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
# SQLALCHEMY_MIGRATE_REPO — это папка, где мы будем хранить файлы SQLAlchemy-migrate.
# db_repository - название этой папки
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 2

