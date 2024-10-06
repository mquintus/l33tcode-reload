# 1813 - Sentence Similarity III
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Case 0 - Equal sentences
        if sentence1 == sentence2: return True

        # Determine shorter and longer
        if len(sentence1) <= len(sentence2):
            shorter = sentence1
            longer = sentence2
        else:
            shorter = sentence2
            longer = sentence1

        # Case 1 - Longer begins with shorter
        for i, word in enumerate(shorter):
            if longer[i] != word:
                break
        else:
            # Also there needs to be a space separating the prependix
            if longer[len(shorter)] == " ":
                return True

        # Case 2 - Longer ends with shorter
        nl = len(longer)
        for i, word in enumerate(shorter[::-1]):
            if longer[nl - i - 1] != word:
                break
        else:
            # Also there needs to be a space separating the appendix 
            if longer[-len(shorter)-1] == " ":
                return True

        # Case 3 - Shorter sentence begins with longer and ends with longer
        pleft = 0
        while shorter[pleft] == longer[pleft]:
            pleft += 1
            if pleft == len(shorter):
                return False
            continue

        # There is a difference 
        # A B  C  D E F 
        # A B (*) * E F

        # First verify that the gap is at a space
        if longer[pleft-1] != " ":
            return False
        if shorter[pleft-1] != " ":
            return False

        # How big is the difference? 
        # The gap must be exactly len(longer) - len(shorter)
        gap = len(longer) - len(shorter)

        # First verify that the gap is at a space at the end!
        if longer[pleft+gap-1] != " ":
            return False

        while pleft < len(shorter) and shorter[pleft] == longer[pleft+gap]:
            pleft += 1
        return pleft == len(shorter)
        
