将 2048项目使用类来封装
    1 核心业务逻辑模块
        Game2048Controller

    2 游戏显示实现模块
        Game2048View

    3 主程序模块
        main.py


'''
1 基于面向对象的程序设计思想
    '以不变应万变' --> 增加程序的可扩展性
    
    1 封装: 分解为不同的类
    2 继承: 隔离变化点与不变的点
        1 抽象出父类
        2 统一行为
        3 重写子类方法
    3 多态: 重写父类中方法

2 模块
    1 导入
        import 模块名 [as 别名]
        from 模块名 import 成员  [as 别名]
        from 模块名 import *
    
    2 加载
        1 被导入时,模块中的所有语句都会执行一次
        2 再次被导入时,不会再次加载模块的语句
        
    3 分类
        第三方模块
            pip install 模块名 -i  python国内镜像源
            
    4 常用的模块
        random
        time
        
3 包 python  package
    导入
        import 包名.模块名 [as 别名]
        from 包名.模块名 import 成员  [as 别名]
        from 包名.模块名 import *
        
    __init__.py文件
        1 标识当前文件夹为python包
        2 限制被导入的模块
        3 在包导入时,会被优先加载
'''