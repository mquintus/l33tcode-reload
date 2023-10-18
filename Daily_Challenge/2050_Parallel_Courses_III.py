# 2050 - Parallel Courses III
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # First we find all courses that have no successor curses.
        # That is our layer 1.
        # We take the max-duration of all curses from layer 1.
        # then we look at layer 2, that is all curses that are precedors of layer 1.
        # Again, 


        is_root = [True for _ in range(n)]
        is_end = [True for _ in range(n)]
        precedors = [[] for _ in range(n)]
        successors = [[] for _ in range(n)]
        pre_time = [0 for _ in range(n)]
        roots = []
        for fro, to in relations:
            to = to - 1
            fro = fro - 1
            precedors[to].append(fro)
            successors[fro].append(to)
            is_root[to] = False
            is_end[fro] = False
            
        for node in range(n):
            if is_root[node]:
                roots.append(node)

        end_of_calculation = False
        while not end_of_calculation:
            end_of_calculation = True
            new_roots = []
        
            for node in [*roots]:
                if len(successors[node]) == 0 and len(precedors[node]) == 0:
                    # This node is final
                    new_roots.append(node)
                    continue

                for follow in successors[node]:
                    end_of_calculation = False
                    pre_time[follow] = max(pre_time[follow], time[node])
                    precedors[follow].remove(node)
                    if len(precedors[follow]) == 0:
                        new_roots.append(follow)
                        time[follow] += pre_time[follow]

            if not end_of_calculation:
                roots = new_roots
        
        
        
        max_time = 0
        for node in roots:
            max_time = max(max_time, time[node])
        
        return max_time

