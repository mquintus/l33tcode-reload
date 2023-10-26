# 823 - Binary Trees With Factors
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9+7
        arr = sorted(arr) 
        n = len(arr)
        dp = {}
        for i in arr:
            dp[i] = 1

        for parent in arr:
            #print(parent, "_", "_", 1)
            for leftChild in arr:
                if leftChild > parent // 2:
                    continue
                if parent % leftChild != 0:
                    continue
                rightChild = parent // leftChild
                if rightChild not in dp.keys():
                    continue
                if rightChild < leftChild:
                    break

                parentSum = dp[leftChild]*dp[rightChild]
                if leftChild != rightChild:
                    parentSum *= 2
                dp[parent]+=(parentSum) % MOD
                #print(parent, leftChild, rightChild, parentSum)

        mySum = 0
        for i in arr:
            mySum += dp[i] % MOD
        return mySum % MOD
