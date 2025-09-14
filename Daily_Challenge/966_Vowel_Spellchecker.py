# 966 - Vowel Spellchecker
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        lowercase = {}
        for s in wordlist[::-1]:
            lowercase[s.lower()] = s

        def vowelReplace(word):
            word = word.lower()
            word = word.replace("a", "*")
            word = word.replace("e", "*")
            word = word.replace("i", "*")
            word = word.replace("o", "*")
            word = word.replace("u", "*")
            return word

        lowercase = {}
        for s in wordlist[::-1]:
            lowercase[s.lower()] = s

        rep = {}
        for s in wordlist[::-1]:
            rep[vowelReplace(s)] = s

        wordlist = set(wordlist)

        #print(rep)
        res = []
        for q in queries:
            if q in wordlist: 
                res.append(q)
            elif q.lower() in lowercase:
                res.append(lowercase[q.lower()])
            elif vowelReplace(q) in rep:
                res.append(rep[vowelReplace(q)])
            else:
                #print("Not found", vowelReplace(q))
                res.append("")

        return res

        
