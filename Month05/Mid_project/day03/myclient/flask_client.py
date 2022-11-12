######################################################
#        > File Name: flask_client.py
#      > Author: GuoXiaoNao
 #     > Mail: 250919354@qq.com 
 #     > Created Time: Mon 20 May 2019 11:52:00 AM CST
 ######################################################

from flask import Flask, send_file
import sys


app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    #首页
    return send_file('templates/index.html')

@app.route('/list.html')
def list():
    #信息列表
    return send_file('templates/list.html')

@app.route('/photo.html')
def photo():
    # 就业喜报
    return send_file('templates/photo.html')

@app.route('/time.html')
def time():
    # 工作时间轴
    return send_file('templates/time.html')

@app.route('/gbook.html')
def gbook():
    # 留言板
    return send_file('templates/gbook.html')

# 应该是学院介绍，目前的about.html是个人信息
# @app.route('/about.html')
# def about():
#     return send_file('templates/about.html')


@app.route('/login')
def login():
    #登录
    return send_file('templates/login.html')

@app.route('/login_callback')
def login_callback():
    #授权登录
    return send_file('templates/oauth_callback.html')

@app.route('/register')
def register():
    #注册
    return send_file('templates/register.html')

# 个人信息
@app.route('/<username>/info')
def info(username):
    #个人信息
    return send_file('templates/about.html')

@app.route('/<username>/change_info')
def change_info(username):
    #修改个人信息
    return send_file('templates/change_info.html')

@app.route('/<username>/change_password')
def change_password(username):
    #修改密码
    return send_file('templates/change_password.html')


@app.route('/<username>/topic/release')
def topic_release(username):
    #发表内容
    return send_file('templates/release.html')


@app.route('/<username>/topics')
def topics(username):
    # 获取个人内容列表 目前没用
    return send_file('templates/list.html')

@app.route('/<username>/topics/detail/<t_id>')
def topics_detail(username, t_id):
    # 文章内容详情
    return send_file('templates/detail.html')


@app.route('/test_api')
def test_api():
    # 测试跨域
    return send_file('templates/test_api.html')

if __name__ == '__main__':
    app.run(debug=True)

