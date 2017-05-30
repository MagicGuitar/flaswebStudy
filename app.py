#!/usr/bin/env python3
# -*-coding:utf-8 -*-
__author__ = 'HZC'
from flask import Flask, render_template  # 渲染模板模块render_template
from flask_script import Manager  # 为flask程序添加了一个命令行解析器
from flask_bootstrap import Bootstrap  # 导入bootstrap框架

app = Flask(__name__)  # 程序实例是Flask类的对象，把接收自客户端的所有请求都交给这个对象处理

manager = Manager(app)  # manager实例
bootstrap = Bootstrap(app)  # bookstrap实例


# -------------------拦截路由---------------------

# 404页面:客户端请求位置页面或路由时显示
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# 500页面:有未处理的异常时显示
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def index():
    return render_template('index.html')


# 动态路由
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)  # 第一个参数是模板的文件名，随后的参数都是键值对


if __name__ == '__main__':
    manager.run()