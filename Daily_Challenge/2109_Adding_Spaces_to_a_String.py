# 2109 - Adding Spaces to a String
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        prev = 0
        for loc in spaces:
            result.append(s[prev:loc])
            prev = loc
        result.append(s[prev:])
        return " ".join(result)
