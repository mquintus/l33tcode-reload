# 2685 - Count the Number of Complete Components
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        edgemap = {i: [] for i in range(n)}
        for f,g in edges:
            edgemap[f].append(g)
            edgemap[g].append(f)

        def get_component(node): 
            component = [node]
            states = [node]
            visited.add(node)
            while states:
                node = states.pop()
                for next_node in edgemap[node]:
                    if not next_node in visited:
                        states.append(next_node)
                        visited.add(next_node)
                        component.append(next_node)
            return component

        connected_component_count = 0
        for i in range(n):
            if i in visited: continue
            full_component = get_component(i)
            size = len(full_component)
            for node in full_component:
                #print(node, size, edgemap[node], len(edgemap[node]))
                if len(edgemap[node]) != size - 1:
                    #print("Break")
                    break
            else:
                #print("Yeah")
                connected_component_count += 1

        return connected_component_count

