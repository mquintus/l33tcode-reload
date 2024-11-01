# 1957 - Delete Characters to Make Fancy String
class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3: return s
        newString = [s[0],s[1]]
        for el in s[2:]:
            if el != newString[-1] or el != newString[-2]:
                newString.append(el)
        return "".join(newString)
        
