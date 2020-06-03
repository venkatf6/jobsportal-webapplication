import os
bd = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Configuration."""
    SECRET_KEY = 'mypython'
    DEBUG = False
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Configuration."""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(bd, 'dev.sqlite')
   