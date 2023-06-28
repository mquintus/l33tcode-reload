class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hashtable = {}
        duplicates = 0
        for row in grid:
            rowhash = "-".join(map(str, row))
            if rowhash in hashtable:
                hashtable[rowhash] += 1
            if rowhash not in hashtable:
                hashtable[rowhash] = 1


        for i in range(len(grid[0])):
            col = [x[i] for x in grid]
            colhash = "-".join(map(str, col))
            if colhash in hashtable:
                duplicates += hashtable[colhash]


        return duplicates


        
