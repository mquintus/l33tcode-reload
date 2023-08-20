class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        '''
        A) Create all MSPS
        B) Identify edges that are in every MSP -> criitical
        C) Return critical vs. pseudo
        '''

        def create_edgelist(my_edges, skipped):
            my_edge_list = [[] for _ in range(n)]
            for i, edge in enumerate(my_edges):
                if i == skipped:
                    continue
                my_edge_list[edge[0]].append([edge[2], edge[0], edge[1], i])
                my_edge_list[edge[1]].append([edge[2], edge[1], edge[0], i])

            for node in range(n):
                my_edge_list[node].sort()
            return my_edge_list
        edge_list = create_edgelist(edges, len(edges))


        global msps
        msps = []
        global smallest_weight
        smallest_weight = 10000000000

        def createMSP(i, nodes, available_edges, used_edges, weight, my_edge_list):
            '''
            We already know a better solution
            '''
            global smallest_weight
            #if weight > smallest_weight:
            #    return smallest_weight

            if i in nodes:
                return smallest_weight

            #print('newly added node', i)
            nodes = [i, *nodes]

            '''
            All nodes are included already.
            '''
            if len(nodes) == n:
                #print("visited nodes", nodes, 'weight', weight)
                #print('Hooray found MSP')
                global msps
                #print('Previous solutions:', msps)
                msps = used_edges
                smallest_weight = weight
                return smallest_weight

            '''
            Now we start at node i
            '''
            for new_edge in my_edge_list[i]:
                if new_edge[2] not in nodes:
                    available_edges.append(new_edge)
            available_edges.sort()

            #print('Current node', i, 'current weight', weight)
            #print("visited nodes", nodes)
            #for edge in available_edges:
            #    print("from", edge[1], end='; ')
            #    print("to", edge[2], end='; ')
            #    print("weight", edge[0], end='; ')
            #    print("edge_id", edge[3])
            #    print('--------------')

        
            least_weight = -1
            for edge in available_edges:
                #if edge[1] != i:
                #    continue 
                if edge[3] in used_edges:
                    continue
                if edge[2] in nodes:
                    continue
                
                if least_weight == -1:
                    least_weight = edge[0]

                #print("least_weight", least_weight, 'considered edge weight:', edge[0])
                #print("from", edge[1], end=' ')
                #print("to", edge[2], end='; ')
                #print("weight", edge[0], end='; ')
                #print("edge_id", edge[3])
                #print('--------------')
                if least_weight == edge[0]:
                    ''' avoid circles '''
                    next_node = edge[2]
                    if next_node not in nodes:
                        #print('next_node', next_node, 'weigth', edge[0], 'previous nodes', nodes)
                        #print('===============')
                        ''' recursive approach '''
                        createMSP(next_node, [*nodes], [*available_edges], [edge[3], *used_edges], edge[0] + weight, my_edge_list)
                    
                    # Now ABORT if we found a solution
                    if len(msps) > 0:
                        return smallest_weight

                if least_weight > edge[0]:
                    # We don't consider the second highest edge cost
                    return smallest_weight
            
        
        createMSP(0, [], [], [], 0, edge_list)
        first_weight = smallest_weight
        used_edges = msps
        critical_edges = set()
        pseudo_edges = set(msps)
        #print(sorted(used_edges))
        #print("first_weight", first_weight)
        for skip_edge in sorted(used_edges):
            smallest_weight = 10000000000
            new_edges = []
            #print("skip_edge", skip_edge, "len(edge_list)", len(edge_list))
            #my_edges = [*edge_list[:skip_edge], *edge_list[skip_edge+1:]]
            #print(my_edges)
            new_edge_list = create_edgelist(edges, skip_edge)
            #print("new_edge_list", new_edge_list)
            createMSP(0, [], [], [], 0, new_edge_list)
            #print("smallest_weight", smallest_weight, msps)
            if smallest_weight > first_weight:
                critical_edges.add(skip_edge)
            #pseudo_edges = pseudo_edges.union(set(msps))

        #print("Known pseudo_edges", pseudo_edges)
        #print("Known critical_edges", critical_edges)

        for edge_id in range(len(edges)):
            a = edges[edge_id][0]
            b = edges[edge_id][1]
            weight = edges[edge_id][2]

            smallest_weight = 10000000000
            
            '''
            We already know about this edge. No need to investigate further.
            '''
            if edge_id in pseudo_edges:
                #print("ABORT")
                continue

            #print("force_edge", edge_id)
            #print("Is it?")


            available_edges = []
            for new_edge in [*edge_list[b], *edge_list[a]]:
                available_edges.append(new_edge)
            available_edges.sort()

            createMSP(a, [b], available_edges, [edge_id], weight, edge_list)
            #print("smallest_weight, first_weight", smallest_weight, first_weight)
            if smallest_weight == first_weight:
                pseudo_edges.add(edge_id)
                #print("It is")
            if smallest_weight > first_weight:
                #pseudo_edges.remove(edge_id)
                #print("It is not")
                pass

            #print("-==-=-=-=-=-=-=-=-=-=-=-=-")



        #print('Critical Edges:', critical_edges)
        #print('pseudo_edges Edges:', pseudo_edges)

                
        pseudo_edges -= critical_edges
        return [sorted(list(critical_edges)), sorted(list(pseudo_edges))]

        

