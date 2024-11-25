# 773 - Sliding Puzzle
def nextSteps(board, zr, zc):
    for d in [(0,1),(1,0),(-1,0),(0,-1)]:
        nr = zr + d[0]
        if nr not in range(max(0, zr-1),min(2, zr+2)): continue
        nc = zc + d[1]
        if nc not in range(max(0, zc-1),min(3, zc+2)): continue
        newboard = [[c for c in row] for row in board]
        newboard[nr][nc],newboard[zr][zc] = newboard[zr][zc],newboard[nr][nc]
        yield newboard


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = [[1,2,3],[4,5,0]]
        if board == target: return 0
        visited = set([tuple([tuple(row) for row in board])])
        states = [(0, board)]
        while states:
            steps, state = states.pop(0)
            #print(steps, state, len(states))
            for r, row in enumerate(state):
                for c, cell in enumerate(row):
                    if cell == 0:
                        for nextBoard in nextSteps(state, r, c):
                            #print(nextBoard)
                            if tuple([tuple(row) for row in nextBoard]) not in visited:
                                visited.add(tuple([tuple(row) for row in nextBoard]))
                                states.append([steps+1, nextBoard])
                                if nextBoard == target: return steps+1
                        continue
        return -1
