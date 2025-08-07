class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        dag = [[] for _ in range(n)]
        inverted_dag = [[] for _ in range(n)]
        def in_distance(size,a,b,c,d):
            return ((a-c)**2 + (b-d)**2 ) <= size**2

        outgoing = [0 for _ in range(n)]

        for i,(x,y,r) in enumerate(bombs):
            for j,(a,b,_) in enumerate(bombs):
                if i == j: continue
                if in_distance(r,x,y,a,b):
                    dag[i].append(j)
                    inverted_dag[j].append(i)
                    outgoing[i] += 1

        #print(dag)

        def dfs(node, visited):
            #print("DFS", node)
            visited[node] = True
            f = 1
            for follow in dag[node]:
                if not visited[follow]:
                    f += dfs(follow, visited)
            return f

        best = 0
        for source in range(n):
            #print('Starting DFS at', source)
            best = max(best, dfs(source, [False]*n))
                

        return best
