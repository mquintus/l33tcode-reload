# 3108 - Minimum Cost Walk in Weighted Graph
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        setCosts = {}
        setMembers = {}
        visited = {}
        
        def joinSets(setIdf,setIdg,c):
            #print(f"join {setMembers[setIdf]} and {setMembers[setIdg]}")
            lt = min(setIdf,setIdg)
            gt = max(setIdf,setIdg)
            #print(f"Old costs {setCosts}")
            setCosts[lt] &= setCosts[gt] & c
            setMembers[lt] |= setMembers[gt]
            for member in setMembers[gt]:
                visited[member] = lt
            del setCosts[gt]
            del setMembers[gt]
            #print(f"New cost {setCosts[lt]}")
        
        for f,g,c in edges:
            #print(f,g,c, setMembers, setCosts)
            if f not in visited and g not in visited:
                #print(f"{f} and {g} not in {visited}")
                newSetId = min(f,g)
                setCosts[newSetId]  = c
                setMembers[newSetId] = set([f,g])
                visited[f] = newSetId
                visited[g] = newSetId
            elif f in visited:
                #print(f"f {f} in {visited}")
                setId = visited[f]
                if g not in visited or visited[g] == setId:
                    #print(f"g {g} not in {visited}")
                    visited[g] = setId
                    #print(f"g {g} setId {setId} len(setMembers) {len(setMembers)} setMembers {setMembers}")
                    setMembers[setId].add(g)
                    #print(f"Old cost {setCosts[setId]}, add {c}")
                    setCosts[setId] &= c
                    #print(f"New cost {setCosts[setId]}")
                else:
                    joinSets(visited[f], visited[g],c)
            elif f not in visited and g in visited:
                #print(f"f {f} not in {visited}, but {g} yes")
                setId = visited[g]
                visited[f] = setId
                setMembers[setId].add(f)
                #print(f"Old cost {setCosts[setId]}, add {c}")
                setCosts[setId] &= c
                #print(f"New cost {setCosts[setId]}")        
        #print(setMembers, setCosts, visited)
        response = []    
        for f,g in query:
            if f == g:
                response.append(0)
            elif not f in visited: 
                #print(f"Not visited {f}")
                response.append(-1)
            elif not g in visited: 
                #print(f"Not visited {g}")
                response.append(-1)
            elif visited[f] != visited[g]:
                response.append(-1)
            elif visited[f] == visited[g]:
                response.append(setCosts[visited[g]])

        return response
