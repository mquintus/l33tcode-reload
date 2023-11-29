# 2147 - Number of Ways to Divide a Long Corridor
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        '''
Intuition:
If only chairs are present, the divisions are deterministic. There is only one option.
Either it's an even number of chairs and then there is one option.
Otherwise it's an uneven number of chairs and then there is no option.
Then: Going from the left, the first wall can be only behind the second seat and before the third seat.
Each plant in between the second and the third chair means an additional option.

        '''
        MOD = 10**9+7
        seats = 0
        plants = 0
        last_chair = 0
        for i, c in enumerate(corridor):
            if c == 'S':
                seats += 1
                last_chair = i
            else:
                plants += 1

        if seats % 2 == 1 or seats == 0:
            return 0

        if plants == 0:
            return 1

        option_global = 1
        options = 1
        seats = 0
        for i, c in enumerate(corridor):
            if seats == 0 and c == 'S':
                seats += 1
            elif seats == 2 and c == 'S':
                seats = 1
                option_global *= options
                option_global %= MOD
                options = 1
            elif seats == 2 and c == 'P':
                options += 1
            elif c == 'S':
                seats = 2
                if i == last_chair:
                    option_global *= options
                    option_global %= MOD
                    break

                
        return option_global % MOD
                
