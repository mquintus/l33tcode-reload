# 881 - Boats to Save People
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Bucket sort
        buckets = [0 for _ in range(limit + 1)]
        for p in people:
            buckets[p] += 1
        for k,v in enumerate(buckets):
            if v > 0:
                print(k, ':', v)
        # Initialize Boat Count
        boat_count = 0

        # Two pointer solution
        p0 = 0
        p1 = limit

        while p1 > p0:
            # Advance pointers through empty buckets
            while buckets[p0] == 0 and p0 < p1:
                p0 += 1
            while buckets[p1] == 0 and p0 < p1:
                p1 -= 1
            
            # If both fit into the boat:
            if p0 == p1 and 2*p0 <= limit and buckets[p0] > 1:
                curr_boats = buckets[p0] // 2
                buckets[p0] -= curr_boats*2
                if buckets[p0] == 1:
                    curr_boats += 1
                    buckets[p0] = 0 
            elif p0 + p1 <= limit:
                curr_boats = min(buckets[p0], buckets[p1])
                buckets[p0] -= curr_boats
                buckets[p1] -= curr_boats
                #print(limit, '|', p0 + p1, '=', p0, '+', p1, '\'', curr_boats )
            else:
                curr_boats = buckets[p1]
                buckets[p1] -= curr_boats
                #print(p1, f'({p0}) =>', p0 + p1, '\'', curr_boats )
            
            boat_count += curr_boats
        return boat_count
            

