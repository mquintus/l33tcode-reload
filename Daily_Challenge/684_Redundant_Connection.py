# 684 - Redundant Connection
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        independent_components = []

        for f,t in edges:
            #print((f,t),independent_components)
            matched = None
            delete = -1
            for i in range(len(independent_components)-1,-1,-1):
                component = independent_components[i]
                if f in component and t in component:
                    return [f,t]
                if f in component or t in component:
                    if matched is None:
                        component.add(t)
                        component.add(f)
                        matched = component
                    else:
                        matched |= component
                        delete = i
                        break
            if delete != -1:
                del independent_components[delete]
            elif matched is None:
                independent_components.append(set())
                independent_components[-1].add(f)
                independent_components[-1].add(t)

        return [-1,-1]

