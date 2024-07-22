# 2418 - Sort the People
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_height = list(zip(heights, names))
        name_height.sort()
        name_height = name_height[::-1]
        return [name for _, name in name_height]
