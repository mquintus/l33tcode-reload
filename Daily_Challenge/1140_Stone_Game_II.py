# 1140 - Stone Game II
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        ninf = float('-inf')
        n = len(piles)
        #dp = [[float('-inf') for i in range(102)] for j in range(1024)]
        dp = {}
        
        def rec(i, m):
            if i < 0 or m < 1:
                raise Exception("")
            if (i,m) in dp:
                return dp[(i,m)]
            if i >= n:
                return 0, [], []

            if i + 2*m >= n:
                #print("i,m,rest",i,m,sum(piles[i:]))
                #dp[(i,m)] = (sum(piles[i:]),piles[i:],[])
                dp[(i,m)] = sum(piles[i:])
                return dp[(i,m)]

            # get + don't get
            best_solution = float("-inf")
            for x in range(1, 2*m+1):
                score = rec(i+x,max(x,m)) # , path_a, path_b = rec(i+x,max(x,m))
                possible_solution = sum(piles[i:i+x]) - score
                #if i == 0 or i == 1 or i == 2:
                #    print("i,x,possible_solution",i,x,possible_solution)
                if possible_solution >= best_solution:
                    best_solution = possible_solution
                    #best_path = [*piles[i:i+x], *path_b]

            #print("selected solution at i", i, best_solution)
            dp[(i,m)] = best_solution
            #dp[(i,m)] = (best_solution, best_path, path_a)
            return dp[(i,m)]
        #diff,path_a,path_b = rec(0,1)
        diff = rec(0,1)
        #print("difference", diff, "all stones",sum(piles),"half sum", sum(piles)/2)
        #print(list(enumerate(piles)))
        #print([(k,v) for k,v in dp.items()])
        #print("Winning bid",diff,path_a,sum(path_a),path_b,sum(path_b))
        return (sum(piles) + diff) //2
