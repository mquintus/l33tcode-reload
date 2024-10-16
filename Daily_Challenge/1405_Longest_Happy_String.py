# 1405 - Longest Happy String
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        prev = ""
        order = [([a], "a"), ([b], "b"), ([c], "c")]
        while a > 0 or b > 0 or c > 0:
            order.sort()
            #print(order)
            #print(res, prev)
            if order[0][0][0] == order[1][0][0] and order[1][0][0] == order[2][0][0]:
                if order[0][1] == prev:
                    res += "".join([order[1][1] + order[2][1] + order[0][1]] * order[0][0][0])
                else:
                    res += "".join([order[0][1] + order[2][1] + order[1][1]] * order[0][0][0])
                return res
            elif order[1][0][0] == order[2][0][0]:
                if order[1][1] != prev:
                    res += order[1][1] + order[2][1]
                    prev = order[2][1]
                else:
                    res += order[2][1] + order[1][1]
                    prev = order[1][1]
                order[2][0][0] -= 1
                order[1][0][0] -= 1
            else:
                if prev != order[2][1] and order[2][0][0] > 1:
                    order[2][0][0] -= 2
                    res += order[2][1] * 2
                    prev = order[2][1]
                elif prev != order[2][1] and order[2][0][0] > 0:
                    order[2][0][0] -= 1
                    res += order[2][1]
                    prev = order[2][1]
                elif prev != order[1][1] and order[1][0][0] > 0:
                    order[1][0][0] -= 1
                    res += order[1][1]
                    prev = order[1][1]
                elif prev != order[0][1] and order[0][0][0] > 0:
                    order[0][0][0] -= 1
                    res += order[0][1]
                    prev = order[0][1]
                else:
                    break
        return res
                

