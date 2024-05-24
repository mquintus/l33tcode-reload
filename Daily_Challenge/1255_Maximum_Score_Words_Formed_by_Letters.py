# 1255 - Maximum Score Words Formed by Letters
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letter_count = Counter(letters)
        words_count = {i: Counter(word) for i, word in enumerate(words)}
        n = len(words)
        
        def recursive(i):
            if i == n:
                return 0

            points = 0
            skip = recursive(i+1)
            take = 0

            can_take = True
            for letter, requirement in words_count[i].items():
                if requirement > letter_count[letter]:
                    can_take = False

            if can_take:
                for letter, requirement in words_count[i].items():
                    letter_count[letter] -= requirement
                    points += score[ord(letter) - ord('a')] * requirement
                take = points + recursive(i+1)

                for letter, requirement in words_count[i].items():
                    letter_count[letter] += requirement
            
            return max(skip, take)

        return recursive(0)
