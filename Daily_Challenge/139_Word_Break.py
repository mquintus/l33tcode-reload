class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        We will compare the beginning of the string with any of the dictionary terms.
        For each match, we will repeat.
        If the remaining string is empty, we were successfull.
        In order to being able to abort early, we will not use recursion but a bfs approach
        with states.

        The state is just were a word ending was found.
        Since we don't want the same state to pop up again, we will keep a register.
        '''

        dp = [False for _ in range(301)]
        states = [0]
        
        while len(states) > 0:
            i = states.pop()
            for word in wordDict:
                end = i+len(word)
                if end >= len(s) + 1:
                    continue
                if dp[end] == True:
                    continue
                if s[i:end] == word:
                    states.append(end)
                    dp[end] = True
                    if end == len(s):
                        return True
        return False
