# 679 - 24 Game
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def myapply(x,y,op):
            if op == "*":
                return x*y
            if op == "/":
                return x/y
            if op == "-":
                return x-y
            if op == "+":
                return x+y

        def check(possible):
            return possible == 24 or possible == 24.0 or abs(possible-24)<0.00001
                
        operators = "*/+-"
        def bracket(a,b,c,d,op0,op1,op2):
            try: 
                possible = myapply(myapply(myapply(a, b, op0), c, op1), d, op2)
                if check(possible): return True
            except:
                pass
            try: 
                possible = myapply(myapply(a, myapply(b, c, op1), op0), d, op2)
                if check(possible): return True
            except:
                pass
            try: 
                possible = myapply(myapply(a, b, op0), myapply(c, d, op1), op2)
                if check(possible): return True
            except:
                pass
            try: 
                possible = myapply(a, myapply(myapply(b, c, op0), d, op1), op2)
                if check(possible): return True
            except:
                pass
            try: 
                possible = myapply(a, myapply(b, myapply(c, d, op0), op1), op2)
                if check(possible): return True
            except:
                pass
            return False

        def solve(a,b,c,d):
            for op0 in operators:
                for op1 in operators:
                    for op2 in operators:
                        possible = bracket(a,b,c,d,op0,op1,op2)
                        if possible: return True
            return False

        possible = False
        for a,b,c,d in itertools.permutations(cards):
            possible |= solve(a,b,c,d)
            if possible: return True
        return False
