'''  用函数的方式实现购物程序
    1、构建商品数据
    2、购物
        1、打印商品数据
        2、输入商品编号及数量
        3、添加购买的商品到购物车
    3、结算
            1、打印购物车中的商品数据
            2、计算已购商品的总价格
            3、输入付款金额，并打印找零
'''

''' 总结:
 重构:
    目的: 主题鲜明, 易于维护
    操作: 将对应的功能封装到函数下(功能单一)

 程序设计思想:
    面向过程: 将问题分解为步骤,逐步实现
'''

commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

list_cart = []


def go_shopping():
    while True:
        choice = input('请输入您的选择[1 购物  2 结算]：')
        if choice == '1':
            shopping()
        elif choice == '2':
            statement()


def shopping():
    # 1 打印商品信息
    print_commodity_info()

    # 2 获取商品的编号
    ccode = get_commodity_id()

    # 3 获取商品的数量
    count = get_commodity_count()

    # 4 添加商品信息
    # list_cart.append({ccode: count})
    list_cart.append({'cid': ccode, 'count': count})


def get_commodity_count():
    '''
        获取商品的数量
    :return: int, 商品的数量
    '''
    while True:
        count = int(input('请输入商品的数量：'))
        if count > 0:  # 购买的数量正确
            return count


def get_commodity_id():
    '''
        获取商品的编号
    :return: int, 商品的编号
    '''
    while True:
        ccode = int(input('请输入商品的编号：'))
        if ccode in commodity_info:  # 商品必须存在
            return ccode


def print_commodity_info():
    '''
        打印商品信息
    :return: None
    '''
    for code, commodity in commodity_info.items():
        print(f'编号：{code}, 名称：{commodity["name"]}, 价格：{commodity["price"]}')


def statement():
    # 1 打印商品信息及计算总价格
    total_money = print_order_total_price()

    # 2 支付
    pay_money(total_money)


def pay_money(total_money):
    '''
        支付结算
    :param total_money: float,应支付金额
    :return: None
    '''
    while True:
        money = float(input(f'本次共消费金额：{total_money},请输入支付的金额：'))
        if money >= total_money:
            print(f'支付成功，找零：{total_money - money}')
            list_cart.clear()  # 清空购物车
            break
        else:
            print('支付失败，请继续支付')


def print_order_total_price():
    '''
        打印商品信息及计算总价格
    :return: float, 应支付金额
    '''
    total_money = 0
    for order in list_cart:
        commodity = commodity_info[order['cid']]   #
        print(f'编号：{order["cid"]}, '
              f'名称：{commodity["name"]}, '
              f'单价：{commodity["price"]}, '
              f'数量：{order["count"]}')

        # for code in order:
        #     commoditys = commodity_info[code]
        #     print(f'编号：{code}, '
        #           f'名称：{commoditys["name"]}, '
        #           f'单价：{commoditys["price"]}, '
        #           f'数量：{order[code]}')

            # pay_money = commoditys["price"] * order[code]
        pay_money = commodity["price"] * order["count"]  # 购买每件商品的价格
        total_money += pay_money  # 累加每件商品的价格
    return total_money


go_shopping()

'''
    购物车：
        存储结构：
            cart = {编号: 数量, ...}    
                判断是否已经买过：
                    是：cart[编号] += 数量
                    否：cart[编号] = 数量
            
            cart = [{编号: 数量}, ...]
                判断是否已经买过：
                    cart.append({编号: 数量})
                    
            cart = [{'cid': 编号, 'count':数量}, ...]
                判断是否已经买过：
                    cart.append({'cid': 编号, 'count':数量})
'''
