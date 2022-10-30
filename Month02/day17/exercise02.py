"""
不改变插入函数与删除函数代码，为其增加验证权限的功能
"""


def verify_permissions(func):
    def wrapper(*args,**kwargs):
        print("验证权限")
        res = func(*args,**kwargs)
        return res
    return wrapper

def insert():
    print("插入")
    return "ok"

def delete(data):
    print("删除")

insert = verify_permissions(insert)
delete = verify_permissions(delete)
print(insert()) # 调用内函数
delete(1001)
