# 1534 - Count Good Triplets
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        result = 0
        for i in range(0, n):
            el_i = arr[i]
            for j in range(i+1, n):
                el_j = arr[j]
                if abs(el_i - el_j) > a:
                    continue
                for k in range(j+1, n):
                    el_k = arr[k]
                    if abs(el_j - el_k) > b:
                        continue
                    if abs(el_i - el_k) > c:
                        continue
                    result += 1
        return result
