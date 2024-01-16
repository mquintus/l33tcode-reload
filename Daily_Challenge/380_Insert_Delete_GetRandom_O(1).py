# 380 - Insert Delete GetRandom O(1)
class RandomizedSet:

    def __init__(self):
        self.order = []
        self.items = {}

    def insert(self, val: int) -> bool:
        vacant = val not in self.items
        if vacant:
            self.items[val] = len(self.order)
            self.order.append(val)
        return vacant

    def remove(self, val: int) -> bool:
        present = val in self.items.keys()
        if not present:
            return False

        position = self.items[val]
        if position == len(self.order) - 1:
            self.order.pop()
            del self.items[val]
        else:
            lastEl = self.order.pop()
            self.items[lastEl] = position
            self.order[position] = lastEl
            del self.items[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.order)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
