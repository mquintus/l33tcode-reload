# 3068 - Find the Maximum Sum of Node Values
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        upgradeable = []
        for val in nums:
            upgrade = (val ^ k) - val
            upgradeable.append(upgrade)
        
        upgradeable.sort()
        
        maxupgrade = 0
        for index in range(len(upgradeable)-1, 0, -2):
            upgrade = upgradeable[index] + upgradeable[index-1]
            if upgrade <= 0:
                break
            maxupgrade += upgrade
        
        return sum(nums) + maxupgrade
