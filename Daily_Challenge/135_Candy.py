class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy_sum = 1
        
        candy_curr = 1
        r_prev = ratings[0]
        last_zero = 1
        last_zero_height = 1000000
        #print("rating", r_prev, "get's candy:", candy_curr)

        for r in ratings[1:]:
            if r < r_prev:
                if candy_curr == 1:
                    candy_sum += last_zero 
                    #print("Increasing previous! by ", last_zero )
                    if last_zero_height <= last_zero:
                        candy_sum += 1
                        #print("and one more ")
                    
                candy_curr = 1
            if r == r_prev:
                last_zero = 0
                last_zero_height = 100000
                candy_curr = 1
            elif r > r_prev:
                last_zero = -1
                candy_curr += 1
                last_zero_height = candy_curr - 1
            candy_sum += candy_curr
            last_zero += 1
            r_prev = r
            #print("rating", r, "get's candy:", candy_curr, "last peak:", last_zero)
        return candy_sum
                
