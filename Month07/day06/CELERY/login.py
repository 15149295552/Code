from backend import send_msg


def login_view():
    print("正在校验用户名和密码~")
    # 发送短信验证码:以celery异步方式执行
    send_msg.delay("13988889999", "871016")
    print("恭喜,注册成功")


login_view()






