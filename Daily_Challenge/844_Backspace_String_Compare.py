# 844 - Backspace String Compare
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Edge cases:
        # - Empty string
        # - Only '#'
        # - ''
        def applyBackspace(myString):
            myString = list(myString)
            write_position = 0
            for p in range(len(myString)):
                if myString[p] == '#':
                    write_position -= 1
                else:
                    myString[write_position] = myString[p]
                    write_position += 1
                if write_position < 0:
                    write_position = 0
            return "".join(myString[:write_position])
        
        s = applyBackspace(s)
        t = applyBackspace(t)
        return s == t


