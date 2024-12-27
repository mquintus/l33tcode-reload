# 1014 - Best Sightseeing Pair
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best1 = (values[0], 0)
        best2 = (values[1], 1)
        best2, best1 = max(best1, best2), min(best1, best2)
        best_score = best1[0] + best2[0] - abs(best1[1] - best2[1])
        #print(best1, best2, best_score)
        for i in range(2,len(values)):
            el = values[i]
            if el + i > best1[0] or best_score < best1[0] + best2[0] - abs(best1[1] - best2[1]):
                best1 = (el, i)
                if el + i > best2[0] + best2[1]:
                    #print(f"{el} + {i} > {best2[0]} + {best2[1]}")
                    best2, best1 = best1,best2
                
                best_score = max(best_score, best1[0] + best2[0] - abs(best1[1] - best2[1]))
                #print(best1, best2, best1[0] + best2[0] - abs(best1[1] - best2[1]))

        return best_score
