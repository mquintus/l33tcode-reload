# 633 - Sum of Square Numbers
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        squares = []
        for i in range(c//2+2):
            sq = i*i
            #print(sq, c-sq)
            if sq == c:
                return True
            if 2*sq == c:
                return True
            squares.append(sq)
            if sq > c:
                break
        #print(squares)
        squares = set(squares)
        for i in range(c//2):
            if c - i*i in squares:
                return True
#            if neg*neg + sq == c:
#                return True
            if i*i > c:
                break

        return False
