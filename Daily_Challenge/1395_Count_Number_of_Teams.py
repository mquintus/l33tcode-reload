# 1395 - Count Number of Teams
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        smaller_left = [0 for _ in range(n)]
        bigger_right = [0 for _ in range(n)]

        smaller_right = [0 for _ in range(n)]
        bigger_left = [0 for _ in range(n)]

        for i in range(n):
            for j in range(i):
                s = rating[i] > rating[j]
                if s:
                    smaller_left[i] += 1
                    bigger_right[j] += 1
                

                b = rating[i] < rating[j]
                if b:
                    smaller_right[j] += 1
                    bigger_left[i] += 1

        #print(smaller_left)
        #print(smaller_right)
        #print(bigger_left)
        #print(bigger_right)

        counter = 0
        for i in range(n):
            counter += smaller_left[i] * bigger_right[i]
            counter += bigger_left[i] * smaller_right[i]

        return counter
