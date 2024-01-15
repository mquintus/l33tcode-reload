# 2225 - Find Players With Zero or One Losses
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        allPlayers = {}
        lostOnce = set()
        notLostAtAll = set()
        for winner, loser in matches:
            if winner not in allPlayers:
                allPlayers[winner] = 0
            if loser not in allPlayers:
                allPlayers[loser] = 0
            allPlayers[loser] += 1
            
            if allPlayers[winner] == 0:
                notLostAtAll.add(winner)
            if allPlayers[loser] == 1:
                lostOnce.add(loser)
                if loser in notLostAtAll: 
                    notLostAtAll.remove(loser)
            if allPlayers[loser] == 2:
                lostOnce.remove(loser)
        return [sorted(list(notLostAtAll)), sorted(list(lostOnce))]
