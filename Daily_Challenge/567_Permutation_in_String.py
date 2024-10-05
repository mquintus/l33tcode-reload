  # 567 - Permutation in String
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        counter = Counter(s1)
        checkcounter = Counter(s2)

        for k,v in counter.items():
            if v > checkcounter[k]: return False

        completed = len(counter.keys())
        valid = True
        
        start = 0
        end = -1

        while end < len(s2):
            if completed == 0: return True

            end += 1
            if end >= len(s2): 
                return False
            endchar = s2[end]

            counter[endchar] -= 1
            if counter[endchar] == 0: completed -= 1
            if counter[endchar] == -1: completed += 1
            valid = counter[endchar] != -1 


            while not valid:
                startchar = s2[start]
                if counter[startchar] == 0: completed += 1
                counter[startchar] += 1
                if counter[startchar] == 0: 
                    completed -= 1
                    valid = True
                if completed == 0:
                    return True
                start += 1
                if start >= len(s2) - len(s1)+1:
                    return False

