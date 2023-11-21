# 1814 - Count Nice Pairs in an Array
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        hashmap = {}

        MOD = 10**9 + 7

        def reverse_num(num):
            return int(f"{num}"[::-1])

        for i,a in enumerate(nums):
            identifier = a - reverse_num(a)
            if identifier not in hashmap:
                hashmap[identifier] = 0
            hashmap[identifier] += 1

        global_count = 0
        for count in hashmap.values():
            if count == 1:
                continue
            combinations = (count * (count-1)) // 2
            global_count += combinations  

        return global_count % MOD
