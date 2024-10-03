# 1590 - Make Sum Divisible by P
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        orig = sum(nums) % p
        remainder = orig % p
        #print("remainder",remainder)
        if remainder == 0: return 0
        
        prefix = [0]
        for el in nums:
            prefix.append((el + prefix[-1])%p)
        prefix = prefix[1:]
        
        hashmap1 = {}
        hashmap2 = {}
        for position, el in enumerate(prefix):
            rem = el % p
            # Store right-most position of remainder of prefixsum
            if rem not in hashmap1:
                hashmap1[rem] = position
            hashmap2[rem] = position
        if 0 not in hashmap1:
            hashmap1[0] = -1
        if 0 not in hashmap2:
            hashmap2[0] = -1

        #print(hashmap)

        bestsolution = float('inf')
        for p1, el in enumerate(prefix):
            missing = (prefix[p1] - remainder + p) %p
            #print("Missing", p1, missing)
            if missing in hashmap1:
                p2 = hashmap1[missing]
                somesolution = p1 - p2
                if somesolution < 0:
                    somesolution = float('inf')
                #print("somesolution", somesolution)
                bestsolution = min(bestsolution, somesolution)
                if bestsolution == 0: return 0
            if missing in hashmap2:
                p2 = hashmap2[missing]
                somesolution = p1 - p2
                if somesolution < 0:
                    somesolution = float('inf')
                #print("somesolution", somesolution)
                bestsolution = min(bestsolution, somesolution)
                if bestsolution == 0: return 0
        
        if bestsolution>=len(nums): return -1
        return bestsolution

        
