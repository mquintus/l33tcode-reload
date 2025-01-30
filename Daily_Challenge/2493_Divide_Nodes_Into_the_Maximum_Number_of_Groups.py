# 2493 - Divide Nodes Into the Maximum Number of Groups
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        groups = []
        not_visited = set(list(range(n)))
        node_to_group = [-1 for i in range(n)]
        edges = [[f-1,t-1] for f,t in edges]
        graph = [[] for i in range(n)]
        for f,t in edges:
            graph[f].append(t)
            graph[t].append(f)

        colors = [-1 for i in range(n)]
        components = []
        while not_visited:
            #print("New component found")
            components.append(set())
            startnode = not_visited.pop()
            components[-1].add(startnode)
            # isBipartite()
            # Coloring
            states = [(startnode,1)]
            colors[startnode] = 1
            while states:
                #print("states",states)
                f, c = states.pop()
                #print(f, not_visited)
                components[-1].add(f)
                for t in graph[f]:
                    if colors[t] == -1:
                        states.append((t, 1-c))
                        colors[t] = 1-c
                        not_visited.discard(t)
                    if colors[t] == c:
                        return -1


        def bfs(f):
            queue = deque()
            visisted = [False for _ in range(n)]
            queue.append(f)
            visisted[f] = True
            distance = 0
            while queue:
                for _ in range(len(queue)):
                    f = queue.popleft()
                    for t in graph[f]:
                        if visisted[t]: continue
                        visisted[t] = True
                        queue.append(t)
                distance += 1
            return distance

        groups = 0
        for component in components:
            currlength = 0
            for f in component:
                currlength = max(currlength, bfs(f))
            groups += currlength

        return groups
