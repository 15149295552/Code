"""
    Python实现单链表
"""


class ListNode:
    """节点类:用来生产节点"""
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkList:
    """单链表类"""
    def __init__(self):
        """初始化一个空链表"""
        self.head = None

    def append(self, item):
        """在链表尾部追加一个节点"""
        node = ListNode(item)
        # 空链表
        if not self.head:
            self.head = node
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        # 循环结束,cur指向尾节点
        cur.next = node

    def travel(self):
        """从头到尾遍历链表"""
        cur = self.head
        while cur:
            print(cur.val, end=" ")
            cur = cur.next

    def remove(self, item):
        """链表中移除一个节点"""
        # 1.空链表
        if not self.head:
            raise Exception("x not in LinkList")

        # 2.头节点
        if self.head.val == item:
            self.head = self.head.next
            return

        # 3.非头节点
        cur = self.head
        try:
            while cur.next.val != item:
                cur = cur.next
        except:
            raise Exception("x not in LinkList")

        cur.next = cur.next.next

    def insert(self, index, item):
        """在指定索引位置添加节点"""
        node = ListNode(item)
        # index=0时
        if index == 0:
            node.next = self.head
            self.head = node
            return

        # index大于链表长度情况
        cur = self.head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        if index >= length:
            self.append(item)
            return

        # 常规情况
        cur = self.head
        for i in range(index - 1):
            cur = cur.next

        node.next = cur.next
        cur.next = node


if __name__ == '__main__':
    ls = LinkList()
    # 创建链表: 100 -> 200 -> 300 -> None
    ls.append(100)
    ls.append(200)
    ls.append(300)
    # 终端1: 100 200 300
    ls.travel()
    print()
    # 终端2: 100 200
    ls.remove(300)
    ls.travel()
    print()
    # 终端3: 100 200 300
    ls.append(300)
    ls.travel()
    print()
    # 终端4: 100 200 300 666
    ls.insert(999, 666)
    ls.travel()
    print()
















