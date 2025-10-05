# 417 - Pacific Atlantic Water Flow
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        nr = len(heights)
        nc = len(heights[0])

        pac = set()
        atl = set()

        for number, mySet in [(0, pac), (1, atl)]:
            #print('.............................................')
            visited = set()
            states = []
            if number == 0:
                states.extend([(heights[0][col],0,col) for col in range(nc)])
                states.extend([(heights[row][0],row,0) for row in range(nr)])
            else:
                states.extend([(heights[nr-1][col],nr-1,col) for col in range(nc)])
                states.extend([(heights[row][nc-1],row,nc-1) for row in range(nr)])
            heapq.heapify(states)

            while states:
                height, row, col = heapq.heappop(states)
                visited.add((row, col))
                #print(height, (row, col))
                mySet.add((row,col))
                for nextrow, nextcol in ((row+1,col),(row-1,col),(row,col+1),(row, col-1)):
                    if nextrow < 0 or nextcol < 0 or nextrow >= nr or nextcol >= nc: continue
                    if (nextrow, nextcol) in visited: continue
                    visited.add((nextrow, nextcol))
                    if heights[nextrow][nextcol] >= heights[row][col]: 
                        heapq.heappush(states, (heights[nextrow][nextcol], nextrow, nextcol))


        result = pac.intersection(atl)
        return [[a,b] for a,b in result]
