# 1653 - Minimum Deletions to Make String Balanced
class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_counter = 0
        min_removals = 0

        for char in s:
            if char == 'a':
                if b_counter > 0:
                    b_counter -= 1
                    min_removals += 1
            else:
                b_counter += 1

        return min_removals
