# 884 - Uncommon Words from Two Sentences
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq1 = Counter(s1.split(' '))
        freq2 = Counter(s2.split(' '))
        set1 = set([word for word in freq1.keys() if freq1[word] <= 1 and freq2[word] <= 1])
        set2 = set([word for word in freq2.keys() if freq2[word] <= 1 and freq1[word] <= 1])
        return list(set1 ^ set2)
