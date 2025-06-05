# 1061 - Lexicographically Smallest Equivalent String
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        equivalency = [set([i]) for i in range(26)]
        for i in range(len(s1)):
            a = ord(s1[i]) - ord('a')
            b = ord(s2[i]) - ord('a')
            if a == b:
                continue
            
            for el in equivalency[a]:
                if el == a: continue
                equivalency[el] |= equivalency[b]
            equivalency[a] |= equivalency[b]
            for el in equivalency[b]:
                if el == b: continue
                equivalency[el] |= equivalency[a]
            equivalency[b] |= equivalency[a]


        equivalency = [sorted(list(i)) for i in equivalency]
        #print(equivalency)
        result = []
        for letter in baseStr:
            result.append(chr(equivalency[ord(letter)-ord('a')][0]+ord('a')))
        
        return "".join(result)



