# 1598 - Crawler Log Folder
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for operation in logs:
            if operation == '../':
                depth = max(0, depth-1)
            elif operation == './':
                pass
            else:
                depth += 1
        return depth
