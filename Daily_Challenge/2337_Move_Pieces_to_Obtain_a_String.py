# 2337 - Move Pieces to Obtain a String
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        i = 0
        for j, el in enumerate(target):
            if el == '_':
                pass
            if el == 'L':
                #print('L found at', j)
                while i < n and start[i] == '_':
                    i += 1
                if i == n: return False
                if start[i] == 'R': return False
                if start[i] == 'L': 
                    if i < j: return False
                    #print('L found at', j, 'can be solved by L at',i)
                    i += 1
                    continue
            if el == 'R':
                #print('R found at', j)
                while i < n and start[i] == '_':
                    i += 1
                if i == n:
                    return False
                if start[i] == 'R': 
                    if i > j: return False
                    #print('R found at', j, 'can be solved by R at',i)
                    i += 1
                    continue
                if start[i] == 'L': return False
        #if i != n:
        #    return False
        for empty in range(i, n):
            if start[empty] != '_': return False
        return True
