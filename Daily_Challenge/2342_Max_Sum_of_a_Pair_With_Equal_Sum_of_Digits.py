# 2342 - Max Sum of a Pair With Equal Sum of Digits
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sum_of_digits(i):
            return sum([int(d) for d in str(i)])
        sod = [sum_of_digits(i) for i in nums]

        hashmap = {}
        best = -1
        for p, el in enumerate(sod):
            if el in hashmap:
                otherindex = hashmap[el]
                best = max(best, nums[otherindex] + nums[p])
                if nums[p] > nums[otherindex]:
                    hashmap[el] = p
            else:
                hashmap[el] = p
            

        return best
