# 316 - Remove Duplicate Letters
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        '''
        This is a tough one.
        Let's say we count how often each letter occurs.
        '''
        latest_occurence = [0] * 123
        for i, char in enumerate(s):
            latest_occurence[ord(char)] = i

        seen = [False] * 123
        stack = []
        for i, char in enumerate(s):
            while (len(stack) > 0
                and (not seen[ord(char)])
                and char < stack[-1] 
                and latest_occurence[ord(stack[-1])] > i): 
                    seen[ord(stack[-1])] = False
                    stack.pop()
            if not seen[ord(char)]:
                stack.append(char)
                seen[ord(char)] = True
        return "".join(stack)
