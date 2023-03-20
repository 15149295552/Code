class ListNode:
    # 节点超级工厂，用来生产二叉树中的节点
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        # 初始化一棵空树:树根为None
        self.root = None

    def add(self, item):
        # 在二叉树增加一个节点
        node = ListNode(item)
        # 空树
        if not self.root:
            self.root = node
            return

        list01 = [self.root]
        while True:
            cur = list01.pop(0)
            # 判断左孩子
            if cur.left:
                list01.append(cur.left)
            else:
                cur.left = node
                break

            # 判断右孩子
            if cur.right:
                list01.append(cur.right)
            else:
                cur.right = node
                break

    def breadth_travel(self):
        """
        广度遍历:从上到下，从左到右
        :return:
        """
        if not self.root:
            return

        list01 = [self.root]
        while list01:
            cur = list01.pop(0)
            print(cur.val, end=" ")
            # 判断左孩子
            if cur.left:
                list01.append(cur.left)
            # 判断右孩子
            if cur.right:
                list01.append(cur.right)

    def pre_travel(self, node):
        """
        前序: 根左右
        :param node: 需要打印的节点
        :return:
        """
        print(node.val, end=" ")
        if node.left:
            self.pre_travel(node.left)
        if node.right:
            self.pre_travel(node.right)

    def mid_travel(self, node):
        """
        中序: 左根右
        :param node: 需要打印的节点
        :return:
        """
        if node.left:
            self.mid_travel(node.left)

        print(node.val, end=" ")

        if node.right:
            self.mid_travel(node.right)

    def last_travel(self, node):
        """
        中序: 左根右
        :param node: 需要打印的节点
        :return:
        """
        if node.left:
            self.last_travel(node.left)

        if node.right:
            self.last_travel(node.right)

        print(node.val, end=" ")


if __name__ == "__main__":
    t = Tree()
    t.add(1)
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    t.add(6)
    t.add(7)
    t.add(8)
    t.add(9)
    # 终端1: 1 2 3 4 5 6 7 8 9
    t.breadth_travel()
    print()
    # 前序: 1 2 4 8 9 5 3 6 7
    # 中序: 8 4 9 2 5 1 6 3 7
    # 后序: 8 9 4 5 2 6 7 3 1
    t.pre_travel(t.root)
    print()
    t.mid_travel(t.root)
    print()
    t.last_travel(t.root)
    print()







