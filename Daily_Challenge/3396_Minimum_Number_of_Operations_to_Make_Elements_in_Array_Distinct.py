# 3396 - Minimum Number of Operations to Make Elements in Array Distinct
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        mySet = set()
        for i, el in enumerate(nums[::-1]):
            if el in mySet:
                break
            mySet.add(el)
        else:
            i += 1

        return (n - i + 2) // 3
