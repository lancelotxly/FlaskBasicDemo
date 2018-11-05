from string import Template

class Config():
    SECRET_KEY = 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:123456@127.0.0.1:3306/test'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = None
    pass

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = None
    pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}