# 641 - Design Circular Deque
class MyCircularDeque:

    def __init__(self, k: int):
        self.store = []
        self.maxl = k

    def insertFront(self, value: int) -> bool:
        if self.maxl == 0:
            return False
        self.store.insert(0, value)
        self.maxl -= 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.maxl == 0:
            return False
        self.store.append(value)
        self.maxl -= 1
        return True

    def deleteFront(self) -> bool:
        if len(self.store) == 0:
            return False
        self.store.pop(0)
        self.maxl += 1
        return True

    def deleteLast(self) -> bool:
        if len(self.store) == 0:
            return False
        self.store.pop()
        self.maxl += 1
        return True
        
    def getFront(self) -> int:
        if len(self.store) == 0:
            return -1
        return self.store[0]

    def getRear(self) -> int:
        if len(self.store) == 0:
            return -1
        return self.store[-1]

    def isEmpty(self) -> bool:
        return len(self.store) == 0

    def isFull(self) -> bool:
        return self.maxl == 0
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
