# 3208 - Alternating Groups II
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:k-1])
        prev = colors[0]
        length = 1
        count = 0
        #print(colors)
        for i in range(1,len(colors)):
            if colors[i] != prev:
                length += 1
            else:
                length = 1
            
            if length >= k:
                count += 1

            prev = colors[i]

        return count

