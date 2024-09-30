class CustomStack:

    def __init__(self, maxSize: int):
        self.mystack = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if self.maxSize == 0: return
        self.maxSize -= 1
        self.mystack.append(x)

    def pop(self) -> int:
        if len(self.mystack) == 0:
            return -1
        self.maxSize += 1
        return self.mystack.pop()
        

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.mystack))):
            self.mystack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
