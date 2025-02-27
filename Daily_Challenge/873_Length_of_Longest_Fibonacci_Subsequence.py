# 873 - Length of Longest Fibonacci Subsequence
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        numbers = set(arr)
        longest = 0
        for i in range(n):
            for j in range(i+1,n):
                a,b=arr[i],arr[j]
                if not a+b in numbers: continue
                count = 2
                while a+b in numbers:
                    count += 1
                    a,b = b,a+b
                    longest = max(longest, count)

        return longest
        
