# 3163 - String Compression III
class Solution:
    def compressedString(self, word: str) -> str:
        c = 1
        prev = word[0]
        newword = []
        for el in word[1:]:
            if c == 9 or el != prev:
                newword.append(f"{c}{prev}")
                c = 0
            c += 1
            prev = el
        newword.append(f"{c}{prev}")
        return "".join(newword)
