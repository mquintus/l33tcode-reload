# 506 - Relative Ranks
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scores = sorted([[b,a] for a,b in enumerate(score)])[::-1]
        places = [[idx, rank] for rank, (points, idx) in enumerate(scores)]
        places[0][1] = "Gold Medal"
        if len(places) >= 2:
            places[1][1] = "Silver Medal"
        if len(places) >= 3:
            places[2][1] = "Bronze Medal"
        for i in range(3, len(places)):
            places[i][1] = str(places[i][1]+1)
        ranks = [rank for idx, rank in sorted(places)]
        return ranks            
