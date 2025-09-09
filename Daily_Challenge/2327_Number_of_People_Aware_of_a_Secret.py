# 2327 - Number of People Aware of a Secret
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD =  1_000_000_007
        hasKnownForDays = [0] * 1001
        hasKnownForDays[0] = 1
        

        for i in range(n-1):
            #print(hasKnownForDays[:forget])
            hasKnownForDays2 = [0] * 1001
            for d, count in enumerate(hasKnownForDays[:forget-1]):
                hasKnownForDays2[d+1] = count % MOD
                if d >= delay-1:
                    hasKnownForDays2[0] += count
            hasKnownForDays = hasKnownForDays2

        return sum(hasKnownForDays) % MOD
