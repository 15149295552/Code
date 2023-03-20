

class ListNode:
    """节点类:用来生产节点"""
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def merge_list(self, head1, head2):
        pre = ListNode(-666)
        cur1 = head1
        cur2 = head2
        new_cur = pre
        while cur1 and cur2:
            if cur1.val >= cur2.val:
                new_cur.next = cur2
                cur2 = cur2.next
            else:
                new_cur.next = cur1
                cur1 = cur1.next

            new_cur = new_cur.next

        # 循环结束，一定有一个链表为None
        if cur1:
            new_cur.next = cur1
        else:
            new_cur.next = cur2

        return pre.next


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




