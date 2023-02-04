from task import send_email


def register_view():
    print("人生得意须尽欢")
    print("莫使金樽空对月")
    # 发送邮件: 推送到redis中
    send_email.delay()

    print("天长地久有时尽，此恨绵绵无绝期")


register_view()












