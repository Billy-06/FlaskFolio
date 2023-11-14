class Config(object):
    """
    Base configuration class. Contains default configuration settings.
    """
    SECRET_KEY = "3318e2107dd74004b6895b817f76fbfd"
    SECRET_KEY = ""
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"
    SQLALCHEMY_ECHO = False

class ProdConfig(Config):
    """
    Production configuration class. Contains configuration settings for a production environment.
    """
    DEBUG = False

class DevConfig(Config):
    """
    Development configuration class. Contains configuration settings for a development environment.
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True