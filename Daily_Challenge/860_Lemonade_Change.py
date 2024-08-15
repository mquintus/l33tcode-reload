# 860 - Lemonade Change
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counts = [0,0]
        for customer in bills:
            if customer == 5:
                counts[0] += 1
            elif customer == 10:
                if counts[0] == 0:
                    return False
                counts[0] -= 1
                counts[1] += 1
            else: #paying with 20
                if counts[0] == 0: return False
                if counts[1] == 0 and counts[0] < 3: return False
                if counts[1] == 0:
                    counts[0] -= 3
                else:
                    counts[1] -= 1
                    counts[0] -= 1
        return True
