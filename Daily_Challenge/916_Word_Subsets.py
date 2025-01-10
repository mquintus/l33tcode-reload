# 916 - Word Subsets
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        a = ord('a')

        wcs1 = []
        for w in words1:
            currcount = [0] * 26
            for letter in w:
                idx = ord(letter)-a
                currcount[idx] += 1
            wcs1.append(currcount)

        wcs2 = [0] * 26
        for w in words2:
            currcount = [0] * 26
            for letter in w:
                idx = ord(letter)-a
                currcount[idx] += 1
                if currcount[idx] > wcs2[idx]:
                    wcs2[idx] = currcount[idx]

        result = []
        for i, wc1 in enumerate(wcs1):
            universal = True
            for lord in range(26):
                if not wc1[lord] >= wcs2[lord]:
                    universal = False
                    break
            else:
                result.append(words1[i])
                
        return result
