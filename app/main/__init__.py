'''
#3 创建蓝本: 通过蓝本实现程序功能，由于只能调用create_app()之后才能使用app.route,太晚了
           因此通过创建蓝本，来达到定义路由的目的，蓝本作用于全局域
           蓝本定义的路由处于休眠状态，只有注册后才被激活， 蓝本在工厂函数中注册到程序上
'''

from flask import Blueprint

main = Blueprint('main',__name__)

from . import view, errors