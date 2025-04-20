# 781 - Rabbits in Forest
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res = 0
        c = Counter(answers)
        for k, v in c.items():
            res += math.ceil(v / (k+1)) * (k+1)
        return res
