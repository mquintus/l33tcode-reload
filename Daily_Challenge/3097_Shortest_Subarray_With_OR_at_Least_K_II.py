# 3097 - Shortest Subarray With OR at Least K II
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def tobytes(bits):
            i = 0
            res = 0
            for bit in bits:
                res += (bit << i)
                i += 1
            return res
        
        def getbits(number):
            res = [0] * 32
            i = 0
            while number > 0:
                res[i] = number & 1
                number >>= 1
                i += 1
            return res

        bitcount = [0] * 32
        currbits = [0] * 32
        currnumber = tobytes(currbits)

        def add_bits(numbits):
            for i in range(32):
                if numbits[i] == 1:
                    bitcount[i] += 1
                    if bitcount[i] == 1:
                        currbits[i] = 1

        def sub_bits(numbits):
            for i in range(32):
                if numbits[i] == 1:
                    bitcount[i] -= 1
                    if bitcount[i] == 0:
                        currbits[i] = 0

        p1 = 0
        p2 = 0
        n = len(nums)
        result = n + 1
        while p2 < n:
            add_bits(getbits(nums[p2])) # [1,1,0,1,0] -> [1 2 4 8 16]
            currnumber = tobytes(currbits)
            #print(p1,p2,currbits,currnumber,k)
            while currnumber >= k:
                result = min(result, p2-p1+1)
                if result == 1: return 1
                sub_bits(getbits(nums[p1]))
                p1 += 1
                currnumber = tobytes(currbits)
            p2 += 1
        if result == n + 1: 
            return -1
        return result


