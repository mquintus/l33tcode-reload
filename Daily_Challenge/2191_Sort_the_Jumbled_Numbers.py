# 2191 - Sort the Jumbled Numbers
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapping = {str(i):str(v) for i,v in enumerate(mapping)}
        trans = str.maketrans(mapping)
        nums.sort(key=lambda i:int(i.__str__().translate(trans)))
        return nums
