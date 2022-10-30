"""
    主模块：程序入口(第一次执行的文件)
"""
from usl import CommodityView

# 只有当前模块是主模块时,才启动项目
# (如果当前模块被其他模块导入,不启动项目)
if __name__ == '__main__':
    view = CommodityView()
    view.main()

