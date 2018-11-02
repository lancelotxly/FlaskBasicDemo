'''
# 1. 建立层次化配置类: 1. 创建基类包含基本配置
                    2. 为开发，测试，生产环境配置不同的数据库
                    3. 私密信息从os.environ中导出
                    4. 注册不同的配置环境
                    5. 定义配置初始化函数
'''
import os

class Config():
    SECRET_KEY = 'hard to guess string' # os.environ.get('SECRET_KEY')
    SQLALCHEMY_COMMIT_ON_TEARDWON = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'stmp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USER_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'defualt': DevelopmentConfig
}
