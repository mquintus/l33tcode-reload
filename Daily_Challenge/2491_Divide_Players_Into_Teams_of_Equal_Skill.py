# 2491 - Divide Players Into Teams of Equal Skill
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        chemsum = 0
        checksum = skill[0] + skill[-1]
        for i in range(n//2):
            chemsum += skill[i] * skill[n-i-1]
            if skill[i] + skill[n-i-1] != checksum:
                return -1
        return chemsum
        
