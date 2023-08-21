class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        '''
        Extend group definition: Each item has a group
        -1 becomes m+1
        '''
        unused_group_id = m
        for i in range(len(group)):
            if group[i] == -1:
                group[i] = unused_group_id
                unused_group_id += 1
                m += 1

        '''
        Get a linked list of items and their precessors
        '''
        after_items = [[] for _ in range(n)]
        before_items = [[] for _ in range(n)]
        for item in range(n):
            for b in beforeItems[item]:
                before_items[item].append(b)
                after_items[b].append(item)

        '''
        Get a linked list of groups and their precessors
        '''
        after_groups = [[] for _ in range(m)]
        before_groups = [[] for _ in range(m)]
        for item in range(n):
            g = group[item]
            for b in beforeItems[item]:
                #print("item, g, b", item, g, b)
                before_group = group[b]
                if before_group != g:
                    ''' A group can't be their own precessor '''
                    before_groups[g].append(before_group)
                    after_groups[before_group].append(g)

        def topologicalSort(after, before_graph):
            visited = []
            before = [len(x) for x in before_graph]
            stack = [node for node in range(len(after)) if before[node] == 0]
            while stack:
                cur = stack.pop()
                visited.append(cur)
                for neib in after[cur]:
                    before[neib] -= 1
                    if before[neib] == 0:
                        stack.append(neib)
            return visited if len(visited) == len(after) else []

        groupOrder = topologicalSort(after_groups, before_groups)
        if groupOrder == []:
            return []
        
        itemOrder = topologicalSort(after_items, before_items)
        if itemOrder == []:
            return []

        grouped_order = [[] for _ in range(m)]
        for item in itemOrder:
            g = group[item]
            grouped_order[g].append(item)

        #print("itemOrder",itemOrder)

        order = []
        for o in groupOrder:
            order.extend(grouped_order[o])
        return order
