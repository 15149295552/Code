from tasks import send_email


def register_view():
    print("正在校验用户名...")
    print("正在存入数据表...")
    # 发送激活邮件：任务 ---> 消息中间件
    send_email.delay()
    print("恭喜您成为尊贵的达达商城用户!")


register_view()










