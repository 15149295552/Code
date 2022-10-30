# 包 package

# 导入
# 方式1: import
# import package01.modu01 as pm1
# import package01.package02.modu02 as ppm1
#
# print(pm1.data)
# pm1.func01()
#
# print(ppm1.data)
# ppm1.func02()


# 方法2: from import
# from package01.modu01 import data, func01
# from package01.package02.modu02 import data, func02
# from package01 import modu01 as md

# print(md.data)
# md.func01()

# print(data)
# func01()

# print(data)
# func02()


# 方式3: from import *
from package01.modu01 import *
# from package01.package02.modu02 import *

# print(data)
# func01()

# print(data)
# func02()


# 从包中找模块
# from package01 import modu01
from package01 import *

# print(modu01.data)


# 从包中找模块,需要在设置包的__init__中,设置需要被导入的模块: __all__ = ['被导入的模块名', ..]
from package01.package02 import *

print(modu02.data)
print(modu21.data)