# 2192 - All Ancestors of a Node in a Directed Acyclic Graph
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        roots = set([i for i in range(n)])
        direct = [[] for i in range(n)] 
        indeg = [0 for i in range(n)]
        for orig, dest in edges:
            direct[orig].append(dest)
            indeg[dest] += 1

            if dest in roots:
                roots.remove(dest)
        
        prevs = [set() for i in range(n)]  
        roots = list(roots)
        #print(direct)
        #return [[]]
        parsed = set()
        print(roots)
        print(indeg)
        #return [[]]
        #counter = 100
        while roots: # and counter:
            #counter -= 1
            somenode = roots.pop(0)
            if somenode in parsed:
                continue
            if indeg[somenode] > 0:
                #print("Not Parsing", somenode)
                roots.append(somenode)
                continue
            #print("Parsing", somenode)
            parsed.add(somenode)
            for nextnode in direct[somenode]:
                indeg[nextnode] -= 1
                #print(nextnode, somenode)
                prevs[nextnode].add(somenode)
                for p in prevs[somenode]:
                    prevs[nextnode].add(p)
                roots.append(nextnode)
            
            

        return [sorted(list(set(p))) for p in prevs]
