# 786 - K-th Smallest Prime Fraction
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        pairs = []
        for i, a in enumerate(arr):
            for b in arr[i+1:]:
                pairs.append([a/b, a, b])
        pairs.sort()
        #print(pairs)
        solution = pairs[k-1]
        return [solution[1], solution[2]]
