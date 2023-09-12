class Solution:
    def minDeletions(self, s: str) -> int:
        appearences = [0] * 26
        a = ord('a')
        for c in s:
            p = ord(c) - a
            appearences[p] += 1
        
        frequency = {}
        max_frequency = 0
        for p in range(26):
            if appearences[p] not in frequency:
                frequency[appearences[p]] = 0    
            frequency[appearences[p]] += 1
            if frequency[appearences[p]] > max_frequency:
                max_frequency = frequency[appearences[p]]

        frequency[0] = 0
        frequencies = list(frequency.items())
        frequencies.sort()
        reductions = 0
        prev_length = frequencies[-1][0]
        overflow = 0
        while len(frequencies):
            m = frequencies.pop()
            length = m[0]
            duplicates = max(0, m[1] - 1)
            #print(m)

            reductions += overflow
            for i in range(prev_length, length + 1, -1):
                overflow -= 1
                overflow = max(0, overflow)
                reductions += overflow
                if overflow <= 0:
                    break


            overflow += duplicates
            prev_length = length
            #print("reductions:", reductions, "overflow:", overflow) 

        return int(reductions)




