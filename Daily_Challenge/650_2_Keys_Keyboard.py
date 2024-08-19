# 650 - 2 Keys Keyboard
class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def recursive(length, clipboard):
            if length == n:
                return 0
            if length > n:
                return float('inf')
            
            if length == clipboard:
                # don't copy! paste
                return 1 + recursive(length + clipboard, clipboard)

            # copy
            copy = 1 + recursive(length, length)
            # if clipboard is empty, only option is to copy           
            if clipboard == 0:
                return copy

            # paste
            paste = 1 + recursive(length + clipboard, clipboard)

            return min(copy, paste)

        return recursive(1,0)

            


            
