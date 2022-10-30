"""
    小结 - 列表基础操作
        创建
            列表名 = [元素1,元素2]
            列表名 = list(可迭代对象)
        添加
            列表名.append(元素)
            列表名.insert(索引,元素)
        定位
            列表名[整数]
            列表名[开始:结束:间隔]
        删除
            del 列表名[索引/切片]
            列表名.remove(元素)
        遍历
            for item in 列表名:
                item存储的是列表元素
            for i in range(len(列表名)):
                i是元素的索引
                列表名[i]是列表元素

"""