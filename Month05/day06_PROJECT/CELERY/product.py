from job import async_send_sms


def login_view():
    print("正在校验用户名...")
    print("正在校验密码...")
    async_send_sms.delay("我爱", "赵丽颖")
    print("登录成功!")


login_view()

