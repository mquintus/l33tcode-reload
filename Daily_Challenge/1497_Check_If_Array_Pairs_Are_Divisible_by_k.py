# 1497 - Check If Array Pairs Are Divisible by k
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if sum(arr) % k != 0:
            return False
        arr = [el % k for el in arr]
        rests = Counter(arr)
        #print(rests)
        for rest, count in rests.items():
            req_rest = (k - rest) % k
            if count != rests[req_rest]:
                return False
        return True
