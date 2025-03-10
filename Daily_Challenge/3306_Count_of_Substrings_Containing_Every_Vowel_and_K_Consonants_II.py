# 3306 - Count of Substrings Containing Every Vowel and K Consonants II
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        nc = []
        p = len(word)
        for i in range(len(word)-1,-1,-1):
            nc.append(p)
            if word[i] != 'a' and word[i] != 'e' and word[i] != 'i' and word[i] != 'o' and word[i] != 'u':
                p = i
        nc = nc[::-1]
        #print(nc)
        x = 0
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        count = 0
        p1 = 0
        p3 = 0
        for p2 in range(len(word)):
            el = word[p2]
            if el == 'a': a+= 1
            elif el == 'e': b+= 1
            elif el == 'i': c+= 1
            elif el == 'o': d+= 1
            elif el == 'u': e+= 1
            else: x += 1

            while x > k:
                el = word[p1]
                if el == 'a': a-= 1
                elif el == 'e': b-= 1
                elif el == 'i': c-= 1
                elif el == 'o': d-= 1
                elif el == 'u': e-= 1
                else: x -= 1
                p1 += 1
            
            while a > 0 and b > 0 and c > 0 and d > 0 and e > 0 and x == k:
                count += nc[p2] - p2
                el = word[p1]
                if el == 'a': a-= 1
                elif el == 'e': b-= 1
                elif el == 'i': c-= 1
                elif el == 'o': d-= 1
                elif el == 'u': e-= 1
                else: x -= 1
                p1 += 1

        return count
