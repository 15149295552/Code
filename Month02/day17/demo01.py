"""
     外部嵌套作用域
"""
c = 30
def func01():
    a = 10
    b = 20
    def func02():
        # 内函数可以读取外部变量
        print(a)
        # 内函数必须通过nonlocal修改外部变量
        nonlocal b
        b = 200
    func02()
    print(b)
# 不能在外部直接调用内部函数
# func02()
func01()