"""
    选择语句
        让代码根据条件,有选择性的执行
        # 写法1
        if 条件:
            满足条件执行的代码
        else:
            不满足条件执行的代码

        # 写法2
        if 条件1:
            满足条件1执行的代码
        elif 条件2:
            不满足条件1,但满足条件2执行的代码
        else:
            以上都不满足执行的代码
"""
# if input("请输入性别:") == "男":
#     print("您好,先生!")
# else:
#     print("您好,女士!")

sex = input("请输入性别:")
if sex == "男":
    print("您好,先生!")
elif sex == "女":
    print("您好,女士!")
else:
    print("性别未知")

# 调试:让代码中断,逐语句审查程序执行过程与变量取值。
# 1. 加断点
# 2. 右键开始调试Debug
# 3. 逐语句执行F8(想目标看现状)







