# 3085 - Minimum Deletions to Make String K-Special
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = deque(sorted(Counter(word).values()))
        #print(freq)

        def solve(freq, fromLeft = True):
            myK = freq[-1] - freq[0]
            #print(freq, myK, k)
            if myK <= k:
                return 0

            # There are two ways: By completely deleting a letter type,
            # or by reducing it's frequency

            deletions = 0

            # deletions to remove the least-frequent letter
            delRemove = float('inf')
            if fromLeft:
                delRemove = freq[0]
                f = freq.popleft()
                delRemove += solve(freq, True)
                freq.appendleft(f) 
            
            # deletions to reduce highest-frequency letter to lowest
            delReduce = max(0, freq[-1] - (freq[0] + k))
            f = freq.pop()
            delReduce += solve(freq, False)
            freq.append(f) 
        
            return min(delReduce, delRemove)

        return solve(freq, True)
