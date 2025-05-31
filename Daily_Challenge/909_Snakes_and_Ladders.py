# 909 - Snakes and Ladders
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board = board[::-1]
        for row in board[1::2]:
            row[:] = row[::-1]
        n = len(board)

        #print(board)

        states = deque([(0,0)])
        while states:
            #print(states)
            steps, field = states.popleft()
            row = field // n
            cell = field % n
            #print(steps, field, row, cell)
            if field == n**2 - 1:
                #print(board)
                return steps

            for i in range(field+1, field+7):
                row = (i) // n
                cell = (i) % n
                field = i
                if field > n**2 -1:
                    continue
                if board[row][cell] < -1:
                    continue
                if board[row][cell] > 0:
                    #print("Ladder", board[row][cell])
                    field = board[row][cell] - 1
                #print("States append", field)
                states.append((steps+1, field))
                board[row][cell] = -(steps+1) * 100
        return -1
            
