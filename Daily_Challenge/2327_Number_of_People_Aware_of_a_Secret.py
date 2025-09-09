# 2327 - Number of People Aware of a Secret
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD =  1_000_000_007
        hasKnownForDays = deque([0] * (forget))
        hasKnownForDays[0] = 1
        count = 1
        telling_people = 0
        for i in range(n-1):
            #print(hasKnownForDays, count, telling_people)
            telling_people -= hasKnownForDays[forget-1]
            telling_people += hasKnownForDays[delay-1]
            count += telling_people
            count -= hasKnownForDays[forget-1]

            hasKnownForDays.appendleft(telling_people % MOD)
            hasKnownForDays.pop()

        #print(hasKnownForDays, count, telling_people)
        return count % MOD
