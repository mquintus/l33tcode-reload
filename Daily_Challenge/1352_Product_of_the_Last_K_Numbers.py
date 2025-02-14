# 1352 - Product of the Last K Numbers
class ProductOfNumbers:

    def __init__(self):
        self.vals = [1]
        self.nullDistance = float('inf')

    def add(self, num: int) -> None:
        prev = self.vals[-1]
        if prev > 0:
            num *= prev
            self.nullDistance += 1
        else:
            self.vals.append(1)
            self.nullDistance = 1
        self.vals.append(num)

    def getProduct(self, k: int) -> int:
        #print(self.vals, k, self.nullDistance)
        if k > self.nullDistance:
            return 0
        return self.vals[-1] // self.vals[-k-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
