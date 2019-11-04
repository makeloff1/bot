import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig(object):

    DEBUG = True
    """sqlalchemy config."""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True
    DATABASE_CONNECTION_OPTIONS = {}

    """database config."""
    POSTGRES_ENV = {
        'user': 'dev',
        'password': 'secret',
        'host': 'postgresql',
        'port': '5432',
        'dbname': 'dev'
    }
    DROP_ON_INIT = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(dbname)s' % POSTGRES_ENV

