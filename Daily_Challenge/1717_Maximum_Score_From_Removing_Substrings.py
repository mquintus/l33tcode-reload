# 1717 - Maximum Score From Removing Substrings
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        score = 0
        top, bot = "a", "b"
        tp, bp = x, y
        if y > x:
            top, bot = "b", "a"
            tp, bp = y, x
        # stack solution
        stack = ['x', 'x']
        i = 0
        #print(tp, bp)
        while i < len(s):
            #print(stack, score)
            char = s[i]
            #print(char)

            if char == bot and stack[-1] == top:
                #print("Remove" , stack[-1], char)
                stack.pop()
                score += tp
                i += 1
                continue
            
            stack.append(char)
            i += 1

        secondstack = ['x']
        for char in stack:
            if secondstack[-1] == bot and char == top:
                score += bp
                secondstack.pop()
            else:
                secondstack.append(char)

        return score
