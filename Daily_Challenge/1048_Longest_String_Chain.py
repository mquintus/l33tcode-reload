# 1048 - Longest String Chain
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def is_predecessor(orig, dest):
            if len(orig) != len(dest) - 1:
                return False
            i = 0
            jump = 0
            for s in dest:
                if s == orig[i]:
                    i += 1
                    if i == len(orig):
                        break
                else:
                    jump += 1
                    if jump > 1:
                        return False
            return True

        words_by_length = {}
        lengths = []
        for w in words:
            l = len(w)
            if not l in words_by_length:
                words_by_length[l] = []
                lengths.append(l)
            words_by_length[l].append(w)
        lengths.sort()

        chains = {}

        max_length = 0
        curr_length = 0
        for l in lengths:
            for w in words_by_length[l]:
                chains[w] = 1
                if l-1 in words_by_length:
                    for w_p in words_by_length[l-1]:
                        if is_predecessor(w_p, w):
                            chains[w] = max(chains[w], 1 + chains[w_p])
                max_length = max(max_length, chains[w])
                if max_length == 16:
                    break

        return max_length
        
        

