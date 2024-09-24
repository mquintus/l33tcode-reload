# 3043 - Find the Length of the Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = set(arr1)
        arr2 = set(arr2)

        prefixes = set()
        for el in arr1:
            while el > 0:
                prefixes.add(el)
                el //= 10

        ml = 0
        for el in arr2:
            while el > 0:
                if el in prefixes:
                    ml = max(ml, len(str(el)))
                    break
                else:
                    el //= 10
        return ml
