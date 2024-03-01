# 2864 - Maximum Odd Binary Number
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        #def sort_solution(s):
        #    s = sorted(s)[::-1]
        #    s = [*s[1:], s[0]]
        #    return "".join(s)

        def one_pass_solution(s):
            count1 = -1
            count0 = 0
            for el in s:
                if el == '0':
                    count0 += 1
                else:
                    count1 += 1
            return "1" * count1 + "0" * count0 + "1"
        return one_pass_solution(s)
