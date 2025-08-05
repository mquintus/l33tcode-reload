# 3477 - Fruits Into Baskets II
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        not_placed = 0
        for i, f in enumerate(fruits):
            for b in range(len(baskets)):
                if baskets[b] >= f:
                    baskets[b] = 0
                    #print("Fruit",i,"in basket",b)
                    break
            else:
                not_placed += 1
        return not_placed
