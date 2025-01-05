# 2381 - Shifting Letters II
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        a = ord('a')
        s = [ord(el) - a for el in s]
        shifts = [[start,end,direction*2-1] for start,end,direction in shifts]

        starts = [(start, direction) for start,end,direction in shifts]
        starts.extend([(end+1, -direction) for start,end,direction in shifts])
        starts.sort()

        curr = 0
        p1 = 0 
        for position in range(len(s)):
            while p1 < len(starts) and starts[p1][0] < position:
                p1 += 1
            while p1 < len(starts) and starts[p1][0] == position:
                curr += starts[p1][1]
                p1 += 1
            s[position] += curr
        
        return "".join([chr((el%26)+a) for el in s])
