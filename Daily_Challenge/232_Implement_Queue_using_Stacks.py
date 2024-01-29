# 232 - Implement Queue using Stacks
class MyQueue:

    def __init__(self):
        self.a = []
        self.b = []

    def push(self, x: int) -> None:
        self.a.append(x)

    def revert(self):
        n = len(self.a)
        for _ in range(n):
            self.b.append(self.a.pop())

    def pop(self) -> int:
        if len(self.b) == 0:
            self.revert()
        return self.b.pop()

    def peek(self) -> int:
        if len(self.b) == 0:
            self.revert()
        return self.b[-1]

    def empty(self) -> bool:
        return len(self.b) == len(self.a) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
