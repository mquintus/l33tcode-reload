# 402 - Remove K Digits
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for el in num:
            intel = int(el)
            
            if intel == 0 and len(stack) == 0:
                continue

            if len(stack) == 0:
                stack.append(el)
                continue
            
            while len(stack) and intel < int(stack[-1]) and k > 0:
                k -= 1
                stack.pop()

            while len(stack) and stack[0] == "0":
                stack.pop(0)

            stack.append(el)

        if k > 0:
            stack = stack[:-k]

        if len(stack) == 0:
            stack = ['0']

        return "".join(stack)
