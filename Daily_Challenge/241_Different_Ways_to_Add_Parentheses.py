# 241 - Different Ways to Add Parentheses
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        dp = [["X"] * 21 for _ in range(21)]

        operators = [False for _ in range(21)]
        for i, c in enumerate(expression):
            if c in ['+', '-', '*']:
                operators[i] = True

        def rec(p,q):
            if q==p: return []
            if dp[p][q] != 'X':
                return dp[p][q]
            if q-p <= 2:
                #print(p,q,[int(expression[p:q])])
                dp[p][q] = [int(expression[p:q])]
                return dp[p][q]
        
            reses = []
            for separator in range(p+1,q):
                if not operators[separator]:
                    continue
                #print(separator, expression[separator])
                lefts = rec(p,separator)
                rights = rec(separator+1,q)
                #print("p,separator+1,q+1",p,separator+1,q)
                #print(lefts, rights,separator)
                op = expression[separator]
                for left in lefts:
                    for right in rights:
                        if op == '+':
                            res = left+right
                        if op == '-':
                            res = left-right
                        if op == '*':
                            res = left*right
                        reses.append(res)
            dp[p][q] = reses
            return dp[p][q]                

        return rec(0,len(expression))
