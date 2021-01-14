import logging
from datetime import timedelta
import os,redis

basedir = os.getcwd()
class Config:
    DEBUG = False
    APP='NEW-SPACE'
    DATABASE = {
        'db': os.environ['DB_NAME'],
        'user': os.environ['DB_USER'],
        'pw': os.environ['DB_PASSWORD'],
        'host': os.environ['DB_HOST'],
        'port': os.environ['DB_PORT'],
    }
    REDIS_URL = {
        'host': os.environ.get('REDIS_HOST','redis'),
        'porta': os.environ.get('REDIS_PORTA','6379'),
        'db': os.environ.get('REDIS_BASE','0'),
    }
    SECRET_KEY = "3c7c70a3-ea26-40df-8ecc-ca78babd2885"
    REDIS_URL = 'redis://%(host)s:%(porta)s/%(db)s' % REDIS_URL
    USE_TZ = True
    CELERY_TIMEZONE = 'UTC'
    CELERY_ENABLE_UTC=True
    CELERY_BROKER_URL = REDIS_URL
    CELERY_RESULT_BACKEND = REDIS_URL
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=60)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % DATABASE
    # SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    SQLALCHEMY_ECHO = False  
    MEDIUM_DATE = "EEEE, d. MMMM y 'at' HH:mm"
    FULL_DATE = "EE dd.MM.y HH:mm"
    LOG_FORMAT = "%(asctime)s %(levelname)s\t: %(message)s"
    BABEL_DEFAULT_LOCALE = 'pt_BR'
    SECURITY_MSG_LOGIN=("", "")
    SECURITY_UNIFIED_SIGNIN=True
    SECURITY_PASSWORD_SALT= "senha001"
    SECURITY_LOGIN_USER_TEMPLATE="/auth/login.html"
    SECURITY_MSG_INVALID_PASSWORD = ("Usuário ou senha invalida", "error")
    SECURITY_USER_IDENTITY_ATTRIBUTES = ('username')
    SECURITY_MSG_INVALID_PASSWORD = ("Usuário ou senha invalida", "error")
    SECURITY_MSG_PASSWORD_NOT_PROVIDED = ("Usuário ou senha invalida", "error")
    SECURITY_MSG_USER_DOES_NOT_EXIST = ("Usuário ou senha invalida", "error")
    SECURITY_MSG_UNAUTHORIZED=("Você não tem permissão para acessar esse recurso.\ncontacte o administrador do sistema!","info")

class DevelopmentConfig(Config):
    FLASK_ENV ='development'
    DEBUG = True
    SQLALCHEMY_ECHO = False

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    SERVER_NAME='localhost'
    DATABASE = {
        'db': os.environ['DB_NAME'],
        'user': os.environ['DB_USER'],
        'pw': os.environ['DB_PASSWORD'],
        'host': os.environ['DB_HOST'],
        'port': os.environ['DB_PORT'],
    }
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % DATABASE
    TESTING = True
    DEBUG=False
    CSRF_ENABLED = False
    WTF_CSRF_ENABLED=False
    SQLALCHEMY_ECHO = False

config = {
    None: DevelopmentConfig,
    'dev': DevelopmentConfig,
    'prod': ProductionConfig,
    'test': TestingConfig
}
