# 1462 - Course Schedule IV
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        startnodes = set([i for i in range(numCourses)])
        indegree = [0 for _ in range(numCourses)]
        processed = [True for _ in range(numCourses)]
        preq = [set() for _ in range(numCourses)]
        edges = [[] for _ in range(numCourses)]
        for f,t in prerequisites:
            edges[f].append(t)
            if processed[t]:
                processed[t] = False
                startnodes.remove(t)
            preq[t].add(f)
            indegree[t] += 1
        
        startnodes = deque(startnodes)
        while startnodes:
            curr = startnodes.pop()
            for nextNode in edges[curr]:
                indegree[nextNode] -= 1
                if indegree[nextNode] == 0:
                    startnodes.append(nextNode)
                preq[nextNode] |= preq[curr]
                preq[nextNode].add(curr)

        result = []
        for f,t in queries:
            result.append(f in preq[t])

        return result
            


        
