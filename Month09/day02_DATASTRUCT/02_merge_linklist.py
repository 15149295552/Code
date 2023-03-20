

class ListNode:
    """节点类:用来生产节点"""
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def merge_list(self, head1, head2):
        pass


if __name__ == '__main__':
    # 链表1: 100 200 600 800
    head1 = ListNode(100)
    head1.next = ListNode(200)
    head1.next.next = ListNode(600)
    head1.next.next.next = ListNode(800)
    # 链表2: 1 200 300
    head2 = ListNode(1)
    head2.next = ListNode(200)
    head2.next.next = ListNode(300)
    # 测试方法
    s = Solution()
    new_head = s.merge_list(head1, head2)
    # 终端1: 1
    print(new_head.val)
    # 终端2: 1 100 200 200 300 600 800
    while new_head:
        print(new_head.val, end=" ")
        new_head = new_head.next




