# 1894 - Find the Student that Will Replace the Chalk
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        #First calculate as many *full* rounds as possible
        full_round = sum(chalk)
        k %= full_round

        # Now let's simulate the last round.
        for student, amount in enumerate(chalk):
            k -= amount
            if k < 0:
                return student
