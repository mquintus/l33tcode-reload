# 947 - Most Stones Removed with Same Row or Column
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # It is possible to remove all stones from a cluster but one stone
        # Therefore this problem can be reduced to just counting the clusters,
        # as one stone per clusters will remain
        # Then to get the number of stones that can be removed, subtract
        # the total amount of stones - number of clusters

        # How do we find a cluster? Set Union Join, but twice, that is over rows and columns
        clusters = []
        for col, row in stones:
            for set_c, set_r in clusters:
                if col in set_c or row in set_r:
                    set_c.add(col)
                    set_r.add(row)
                    break
            else:
                clusters.append([set([col]), set([row])])

        active_union = True
        while active_union:
            active_union = False
            for i, cluster in enumerate(clusters):
                active_rows = cluster[0]
                active_cols = cluster[1]
                join = False
                for j, anothercluster in enumerate(clusters[i+1:]):
                    for row in anothercluster[0]:
                        if row in active_rows:
                            join = True
                            break
                    if join:
                        break
                    for col in anothercluster[1]:
                        if col in active_cols:
                            join = True
                            break
                    if join:
                        break
                if join:
                    cluster[0] |= anothercluster[0]
                    cluster[1] |= anothercluster[1]
                    del clusters[i+j+1]
                    active_union = True
                    break

        return len(stones) - len(clusters)
        
