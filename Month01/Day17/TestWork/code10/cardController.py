# 名片核心业务处理模块

class CardController:
    def __init__(self):
        self.__list_card = []  # 存储名片对象

    @property
    def list_card(self):  # 读取方法(在视图类中仅允许访问,不允许修改)
        return self.__list_card

    def add_card_data(self, card):
        '''
            添加名片对象
        :param card: object, 名片对象
        :return: str, 当id重复则返回字符串,否则返回None
        '''
        # list_card_id = [c.id for c in self.__list_card]
        list_card_id = list(map(lambda c: c.id, self.__list_card))
        if card.id not in list_card_id:
            self.__list_card.append(card)
        else:
            return 'ID重复,请重新输入'

    def modify_card_data(self, new_card):
        '''
            根据携带的名片数据对象修改现存对象的数据
        :param new_card: object,携带修改数据的名片对象
        :return: bool,修改成功返回True,否则返回False
        '''
        for c in range(len(self.__list_card)):
            if self.__list_card[c].id == new_card.id:  # 判断是要修改的名片对象
                self.__list_card[c] = new_card
                return True
        return False

    def delete_card_data(self, del_id):
        '''
            根据id删除对应的名片对象
        :param del_id: int,要删除的id
        :return: bool,删除成功返回True,否则返回False
        '''
        for c in self.__list_card:
            if c.id == del_id:
                self.__list_card.remove(c)
                return True
        return False

    def query_card_data(self, conditon, value):
        '''
            根据条件及值查询对应的名片对象
        :param conditon: function,条件函数
        :param value: any, 值
        :return: generator, 生成器
        '''
        for c in self.__list_card:
            if conditon(c, value):
                yield c
