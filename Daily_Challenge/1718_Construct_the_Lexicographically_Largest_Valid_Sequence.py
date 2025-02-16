# 1718 - Construct the Lexicographically Largest Valid Sequence
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        l = n*2-1
        solution = [-1]*l
        numbers = list(range(1,n+1))[::-1]
        visited = [False]*(n+1)

        def rec(position, v):
            if v == n:
                return True
            if position == l:
                return False

            if solution[position] != -1:
                success = rec(position+1,v)
                return success 

            #print(position, v)

            for el in range(n,0,-1):
                #print(el)
                if visited[el]: continue
                if el > 1:
                    if position+el >= l: continue
                    if solution[position] != -1 or solution[position+el] != -1: continue
                    solution[position] = el
                    solution[position+el] = el
                if el == 1:
                    if solution[position] != -1: continue
                    solution[position] = el

                visited[el] = True
                success = rec(position+1,v+1)
                if success: return True
                visited[el] = False
                if el > 1:
                    solution[position+el] = -1
                solution[position] = -1

            return False 
        rec(0, 0)
        return solution
