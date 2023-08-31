class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # reencode ranges 
        newRanges = []
        for i, r in enumerate(ranges):
            newRanges.append([i-r, i+r])
        newRanges.sort()
        
        #print(newRanges)

        def would_it_work(l,r,unmatched,would_work):
            if l <= unmatched and r >= unmatched:
                # this one would work
                if r > would_work[1]:
                    would_work = [l, r]
                    #print(' would work. Selected.', end=' ')
                #else:
                    #print(' would work', end=' ')
            return would_work

        would_work = [-1, -1]
        counter = 0
        unmatched = 0        
        for l, r in newRanges:
            #print()
            #print("Unmatched:", unmatched, "check tap", (l,r,), end=' ')

            would_work = would_it_work(l,r,unmatched,would_work)
                    
                    
            if l > unmatched:
                # does not work.
                # Lets use the one that would work
                if would_work[0] <= unmatched and would_work[1] >= unmatched:
                    counter += 1
                    #print()
                    #print("Selected", would_work)
                    unmatched = would_work[1]
                    if unmatched >= n:
                        return counter

                    would_work = would_it_work(l,r,unmatched,would_work)
                else:
                    return -1



        if would_work[0] <= unmatched and would_work[1] >= unmatched:
            #print()
            #print("Selected", would_work)
            counter += 1
            unmatched = would_work[1]
            if unmatched >= n:
                return counter
        return -1
                

            

