# 名片视图展示类
import sys

from Day17.TestWork.code10.cardController import CardController
from Day17.TestWork.code10.cardModel import CardModel


class CardView:
    def __init__(self):
        self.__controller = CardController()

    @staticmethod
    def __display_menu():
        print('1 查看名片数据')
        print('2 增加名片数据')
        print('3 更新名片数据')
        print('4 删除名片数据')
        print('5 查询名片数据')
        print('6 退出名片系统')
        print('-' * 30)

    def __user_choice(self):
        choice = input('请输入功能序号:')
        if choice == '1':
            self.__show_card_data(self.__controller.list_card)
        elif choice == '2':
            self.__append_card_data()
        elif choice == '3':
            self.__update_card_data()
        elif choice == '4':
            self.__remove_card_data()
        elif choice == '5':
            self.__find_card_data()
        elif choice == '6':
            sys.exit('谢谢使用!!!')

    def __show_card_data(self, card_data):
        '''
            显示名片数据
        :param card_data: list,名片数据
        :return: None
        '''
        print('-' * 30)
        for card in card_data:
            print('{}-{}-{}-{}-{}'.format(*card.__dict__.values()))
        print('-' * 30)

    def __append_card_data(self):
        '''
            添加名片信息
        :return: None
        '''
        while True:
            id = input('请输入名片ID:')
            if not id:
                break
            name = input('请输入姓名:')
            company_name = input('请输入公司名:')
            phone = int(input('请输入名片电话:'))
            job = input('请输入职位:')
            card = CardModel(name, company_name, phone, job, int(id))
            self.__controller.add_card_data(card)

    def __update_card_data(self):
        '''
            更新名片信息
        :return: None
        '''
        while True:
            id = input('请输入名片ID:')
            if not id:
                break
            name = input('请输入更新的姓名:')
            company_name = input('请输入更新的公司名:')
            phone = int(input('请输入更新的名片电话:'))
            job = input('请输入更新的职位:')
            card = CardModel(name, company_name, phone, job, int(id))
            if self.__controller.modify_card_data(card):
                print('修改成功!!!!!')
            else:
                print('修改失败.....')

    def __remove_card_data(self):
        '''
            删除名片对象
        :return: None
        '''
        while True:
            del_id = int(input('请输入删除的名片ID:'))
            if self.__controller.delete_card_data(del_id):
                print('删除成功....')
                break
            else:
                print('删除失败.....')

    def __find_card_data(self):
        '''
            查询职位数据
        :return: None
        '''
        job = input('请输入查询的职位信息:')
        func = lambda card, value: value in card.job
        for c in self.__controller.query_card_data(func, job):
            print(c.__dict__)

    def main(self):
        while True:
            CardView.__display_menu()
            self.__user_choice()