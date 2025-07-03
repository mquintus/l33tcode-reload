# 3304 - Find the K-th Character in String Game I
class Solution:
    def kthCharacter(self, k: int) -> str:
        word = ['a', 'b', 'b', 'c', 'b', 'c', 'c', 'd', 'b', 'c', 'c', 'd', 'c', 'd', 'd', 'e', 'b', 'c', 'c', 'd', 'c', 'd', 'd', 'e', 'c', 'd', 'd', 'e', 'd', 'e', 'e', 'f', 'b', 'c', 'c', 'd', 'c', 'd', 'd', 'e', 'c', 'd', 'd', 'e', 'd', 'e', 'e', 'f', 'c', 'd', 'd', 'e', 'd', 'e', 'e', 'f', 'd', 'e', 'e', 'f', 'e', 'f', 'f', 'g', 'b', 'c', 'c', 'd', 'c', 'd', 'd', 'e', 'c', 'd', 'd', 'e', 'd', 'e', 'e', 'f', 'c', 'd', 'd', 'e', 'd', 'e', 'e', 'f', 'd', 'e', 'e', 'f', 'e', 'f', 'f', 'g', 'c', 'd', 'd', 'e', 'd', 'e', 'e', 'f', 'd', 'e', 'e', 'f', 'e', 'f', 'f', 'g', 'd', 'e', 'e', 'f', 'e', 'f', 'f', 'g', 'e', 'f', 'f', 'g', 'f', 'g', 'g', 'h']
        k -= 1
        while k > len(word) - 1:
            for letter in word[:len(word)]:
                newLetter = chr(ord(letter) + 1)
                if letter == 'z': newLetter = 'a'
                word.append(newLetter)
        return word[k]


