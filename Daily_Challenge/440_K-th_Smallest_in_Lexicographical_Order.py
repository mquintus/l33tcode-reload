# 440 - K-th Smallest in Lexicographical Order
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def number_of_children(numl):
            number = int("".join([str(i) for i in num]))
            return number_of_c(number*10,number*10+9)
        @cache
        def number_of_c(lower_bound,upper_bound):
            this_level_diff = upper_bound - lower_bound + 1
            #print("Lower bound, upper bound,",lower_bound,upper_bound)
            if lower_bound > n:
                return 0
            if upper_bound >= n:
                #print("Reached n", n, upper_bound)
                upper_bound = n
                return upper_bound - lower_bound + 1
            
            res = (this_level_diff) + number_of_c(lower_bound*10, upper_bound*10+9)
            #print("Returning",res)
            return res

        k -= 1
        num = [1]
        ctr = 1000
        while k > 0 and ctr > 0:
            ctr -= 1
            number = int("".join([str(i) for i in num]))
            #print(num, k, number_of_children(num))
            if number_of_children(num) >= k:
                # Down
                #print(num, k)
                num.append(0)
                k -= 1
            elif number_of_children(num) < k:
                # Right
                k -= number_of_children(num)
                k -= 1
                num[-1] += 1
                #for i in range(len(num)):
                #    num[i] += 1
            #print(num, k)

        return int("".join([str(i) for i in num]))
