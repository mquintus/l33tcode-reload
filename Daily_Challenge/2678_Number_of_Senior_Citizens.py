# 2678 - Number of Senior Citizens
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum([1 for citizen in details if int(citizen[11:13]) > 60])
