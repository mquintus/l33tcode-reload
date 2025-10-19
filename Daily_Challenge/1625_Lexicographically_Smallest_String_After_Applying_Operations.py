# 1625 - Lexicographically Smallest String After Applying Operations
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited = set()

        def rotate(s):
            return s[b:] + s[:b]

        def add(s):
            return "".join(["".join(sub) for sub in zip(s[::2], [str((a+int(x))%10) for x in s[1::2]])])

        def dfs(s):
            nex = rotate(s)
            if nex not in visited:
                visited.add(nex)
                dfs(nex)

            nex = add(s)
            if nex not in visited:
                visited.add(nex)
                dfs(nex)

        dfs(s)
        return min(visited)
            
