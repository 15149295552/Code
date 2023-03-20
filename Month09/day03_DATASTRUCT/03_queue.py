"""
    题目：用两个栈实现一个队列，完成队列的 push 和 pop 操作。
"""


class Solution:
    # 顺序栈：append() + pop() 组合
    stack1 = []
    stack2 = []

    def push(self, item):
        # 入队
        self.stack1.append(item)

    def pop(self):
        # 出队
        if self.stack2:
            return self.stack2.pop()

        if self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

            return self.stack2.pop()

        raise Exception("pop from empty queue")


if __name__ == "__main__":
    s = Solution()
    # 入队: 100 200 300 400
    s.push(100)
    print(s.pop())
    s.push(200)
    s.push(300)
    print(s.pop())
    s.push(400)
    print(s.pop())
    print(s.pop())
    print(s.pop())















