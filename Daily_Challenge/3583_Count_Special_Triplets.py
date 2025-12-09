# 3583 - Count Special Triplets
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        freqPrev = dict()
        freqNext = Counter(nums)

        total = 0
        n = len(nums)
        for i in range(0, n):
            el = nums[i]
            freqNext[el] -= 1

            doubl = 2 * el

            #print(freqPrev, freqNext, "Looking for", doubl)

            #print("looking for ", doubl)
            if doubl in freqPrev and doubl in freqNext:
                total += freqNext[doubl] *  freqPrev[doubl]
                total %= MOD

            if el not in freqPrev:
                freqPrev[el] = 0
            freqPrev[el] += 1

        return total % MOD


