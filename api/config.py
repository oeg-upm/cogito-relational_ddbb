import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY") or "string hard to guess"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # In case you want to pass more configurations to the app
    @staticmethod
    def init_app():
        pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URI") or "sqlite:///" + os.path.join(basedir, "data-dev.sqlite")
    FLASK_DEBUG = True

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI") or "sqlite:///"
    FLASK_TESTING = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DATABASE_URI") or "sqlite:///" + os.path.join(basedir, "data.sqlite")
    

config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}