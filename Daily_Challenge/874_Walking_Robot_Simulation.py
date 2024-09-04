# 874 - Walking Robot Simulation
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set([(b,a) for a,b in obstacles])
        row_has_obstacles = set()
        col_has_obstacles = set()
        for a,b in obstacles:
            row_has_obstacles.add(a)
            col_has_obstacles.add(b)
        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        maxdistance = 0
        d = 2
        row = 0
        col = 0
        for command in commands:
            if command == -2:
                d = (d - 1) % 4
                continue
            if command == -1:
                d = (d + 1) % 4
                continue
            drow, dcol = directions[d]
            steps = command
            if row not in row_has_obstacles and col not in col_has_obstacles:
                row += drow * steps
                col += dcol * steps
            else:
                for _ in range(steps):
                    if (drow + row, dcol+col) in obstacles:
                        #print("Run into obstacle " , (drow + row, dcol+col))
                        break
                    row += drow
                    col += dcol
            distance = row**2 + col**2
            maxdistance = max(distance,maxdistance)
        return maxdistance
