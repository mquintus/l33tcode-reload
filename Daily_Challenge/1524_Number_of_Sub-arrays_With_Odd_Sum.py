# 1524 - Number of Sub-arrays With Odd Sum
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        arr = [el % 2 for el in arr]
        MOD = 10**9 + 7
        
        prefixsum = [arr[0]]
        for el in arr[1:]:
            prefixsum.append((el + prefixsum[-1])%2)

        #print(prefixsum)
        count_odd = 0
        count_even = 1
        count = 0
        for i in range(0, len(prefixsum)):
            #print(prefixsum[i], count_even, count_odd, count)
            if prefixsum[i] == 1:
                count += count_even
                count_odd += 1
            elif prefixsum[i] == 0:
                count += count_odd
                count_even += 1
        return count % MOD
