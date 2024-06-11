# 1122 - Relative Sort Array
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        set2 = set(arr2)
        pos2 = {val: pos for pos, val in enumerate(arr2)}
        arr3 = sorted([val for val in arr1 if val not in set2])

        result = [val for val in arr1 if val in set2]
        result.sort(key=lambda val: pos2[val])
        result.extend(arr3)

        return result
