# 474 - Ones and Zeroes
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        newstrs = []
        for i in range(len(strs)):
            zeroes, ones = (strs[i].count("0"),strs[i].count("1"))
            #if zeroes > m or ones > n:
            #    continue
            newstrs.append( (zeroes, ones, ))

        strs = newstrs

        dp = [[[-1] * 101 for _ in range(101) ]for _ in range(601) ]

        #print(strs)
        glob_longest = 0
        longest = 0
        def dfs(i, a, b, length):
            if i == len(strs):
                return 0

            if dp[i][a][b] != -1:
                return dp[i][a][b]

            # take
            zeroes, ones = strs[i]
            zeroes += a
            ones += b
            take = 0
            if zeroes <= m and ones <= n:
#                print("Position", i, "Take", zeroes, ones)
                take = 1 + dfs(i + 1, zeroes, ones, length + 1)


            # skip
            skip = dfs(i + 1, a, b, length)
            
            longest = max(skip, take)

            dp[i][a][b] = longest
            nonlocal glob_longest
            #print("Longest", longest)
            glob_longest = max(glob_longest, longest)
            return longest

        dfs(0, 0, 0, 0)
        return glob_longest
