# 664 - Strange Printer
class Solution:
    def strangePrinter(self, s: str) -> int:
        def removeDuplicates(s):
            news = s[0]
            p = 1
            while p < len(s):
                if s[p] != news[-1]:
                    news += s[p]
                p += 1
            return news
        s = removeDuplicates(s)

        n = len(s)

        dp = [[0 for i in range(n+1)] for j in range(n+1)]

        def getOp(left, right):
            if dp[left][right] != 0:
                return dp[left][right]
            if right <= left:
                return 0
            if right == left+1:
                return 1
            ops = float('inf')
            for m in range(left+1, right):
                op1 = getOp(left,m)
                op2 = getOp(m,right)
                ops = min(op1+op2, ops)
            if s[left] == s[right-1]:
                ops -= 1
            dp[left][right] = ops
            return ops
            
            
        return getOp(0,n)
                
