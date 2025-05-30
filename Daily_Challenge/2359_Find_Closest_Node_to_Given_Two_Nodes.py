# 2359 - Find Closest Node to Given Two Nodes
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        distances1 = [float('inf')] * n
        distances2 = [float('inf')] * n

        distances1[node1] = 0
        node = edges[node1]
        c = 0
        while node != -1:
            #print(node)
            c += 1
            if distances1[node] <= c:
                break
            distances1[node] = c
            node = edges[node]


        #print()
        distances2[node2] = 0
        node = edges[node2]
        c = 0
        while node != -1:
            #print(node)
            c += 1
            if distances2[node] <= c:
                break
            distances2[node] = c
            node = edges[node]
        
        result = float('inf')
        minDistNode = -1
        for i in range(n):
            if result > max(distances1[i], distances2[i]):
                result = max(distances1[i], distances2[i])
                minDistNode = i
        
        #print(distances1)
        #print(distances2)

        #if result == float('inf'):
        #    return -1
        return minDistNode
