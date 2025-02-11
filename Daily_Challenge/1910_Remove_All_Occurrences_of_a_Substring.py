# 1910 - Remove All Occurrences of a Substring
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        part = list(part)
        n = len(part)
        myStack = []
        for el in s:
            #print(myStack)
            myStack.append(el)
            while myStack[-n:] == part:
                myStack = myStack[:-n]
        return "".join(myStack)
