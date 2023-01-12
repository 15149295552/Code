"""
    xpath
        在需要查找的内容上右键-检查
        如果html标签没有唯一性
        那么需要向上逐节点寻找唯一性
        再逐节点回到需要查找的内容


    -- 所有搜索引擎链接：
                    //div[@class="search_nav clearfloat"]//a
                    //div[@class="search_nav clearfloat"]/ul/li/a
    -- 网站维护/运营维护/所有链接
                    //div[@class="listbar clearfloat"]/div[2]//a



"""