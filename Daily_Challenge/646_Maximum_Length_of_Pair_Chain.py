class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        '''
        Greedy approach is optimal
        '''
        
        pairs.sort(key=lambda x: [x[1], x[0]])

        end = -1001
        result = 0
        for i in range(len(pairs)):
            if end < pairs[i][0]:
                result += 1
                end = pairs[i][1]
            
        return result
