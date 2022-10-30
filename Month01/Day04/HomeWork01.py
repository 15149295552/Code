'''
模拟网页登录，编写实现逻辑。
    设定初始的一个用户名与密码，【限定有3次】用户名及密码的验证机会，在3次机会内能输入正确，则打印登录成功；在3次机会内：如果用户名与密码都错误，则需用户重新录入用户名与密码；如果用户正确，则仅需验证密码；同时在3次机会内需提示用户剩余多少次机会；最后当3次机会使用完毕，则打印账号被锁定；

分析：
    1 设置初始的用户名与密码
    2 第1次：输入用户名与密码（校验）
        times = 0

        while times < 3:
            user_name = input('请输入用户名：')
            user_pwd = input('请输入密码：')
            times += 1
            if 用户名正确：
                if 密码正确：
                    print('登录成功')
                    break
                else:  # 用户名正确，密码错误
                    while times < 3:
                        user_pwd = input('请输入密码：')
                        times += 1

                        if 密码正确：
                            print('登录成功')
                            break
                        else:
                            print('密码错误')
                    else:   # 用户名输入错误（3次机会消耗完毕）
                        print('账号被锁定')
                    break
            else:
                print('用户名或密码错误')
        else:   # 用户名输入错误（3次机会消耗完毕）
            print('账号被锁定')
'''

init_name = 'tedu'
init_pwd = '123'

times = 0

while times < 3:
    user_name = input('请输入用户名：')
    user_pwd = input('请输入密码：')
    times += 1
    if user_name == init_name:  # 用户名正确
        if user_pwd == init_pwd:  # 密码正确
            print('登录成功')
            break
        else:  # 用户名正确，密码错误
            print('密码错误', '剩余：', 3 - times, '次机会')
            while times < 3:
                user_pwd = input('请输入密码：')
                times += 1

                if user_pwd == init_pwd:  # 密码正确
                    print('登录成功')
                    break   # 终止内层循环
                else:
                    print('密码错误', '剩余：', 3-times, '次机会')
            else:
                print('账号被锁定（密码3次输入错误）')

            break    # 终止外层循环
    else:   # 用户名错误
        print('用户名或密码错误', '剩余：', 3-times, '次机会')
else:
    print('账号被锁定（用户名3次输入错误）')

