# 1399 - Count Largest Group
class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = {}

        for i in range(1,n+1):
            curr = sum([int(c) for c in str(i)])
            #print(i, curr)
            if curr not in groups:
                groups[curr] = 0
            groups[curr] += 1
        
        biggest = max(groups.values())
        
        #print(biggest)
        #print(groups)
        res = 0
        for k,v in groups.items():
            if v == biggest:
                res += 1

        return res
