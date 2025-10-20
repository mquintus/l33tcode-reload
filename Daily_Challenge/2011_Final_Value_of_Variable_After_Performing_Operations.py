# 2011 - Final Value of Variable After Performing Operations
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:
            if op[1] == '+':
                x += 1
            else:
                x -= 1
        return x
