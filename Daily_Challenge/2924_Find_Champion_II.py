# 2924 - Find Champion II
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        champs = [True for _ in range(n)]
        champcount = n
        for win, loose in edges:
            if champs[loose]:
                champs[loose] = False
                champcount -= 1
        if champcount > 1: return -1
        for i in range(n):
            if champs[i]:
                return i
        
