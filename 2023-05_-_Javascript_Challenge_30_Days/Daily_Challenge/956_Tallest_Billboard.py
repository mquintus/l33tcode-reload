class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        # this looks like a typical dynamic programming problem
        # related to the knapsack problem.
        # 
        # The fact that rods can't be longer than 20
        # and there are at max 1000 rods with a combined length of only up to 5000
        # is a clue that we might even accept quadratic time complexity.

        # also it is a take-or-skip problem.
        # In any state, you can use the rod for either stack1 or stack2 or not at all.

        # Idea: 
        # The height can't be larger than the half of the sum of all rods.
        
        # Also:
        # If we ever only keep track of the diff between stack1 and stack2
        # we can better memoize.
        my_hashmap = [[None for i in range(10001)] for j in range(len(rods))]

        def use_rods(i, diff, maxlength) -> int:
            if len(rods) == i:
                if diff == 0:
                    return 0
                return -100000

            if diff > maxlength:
                return -100000
            if diff < -maxlength:
                return -100000

            #
            # This is for the second and third option 
            # (stack2 or don't pick);
            # if it leads to the same diff, don't follow this lead
            # because a larger value (stack1) has already been found
            # with the same diff.
            if my_hashmap[i][diff + 5000] is not None:
                return my_hashmap[i][diff + 5000]

            maxHeight = max(
                rods[i] + use_rods(i + 1, diff + rods[i], maxlength),
                rods[i] + use_rods(i + 1, diff - rods[i], maxlength),
                use_rods(i + 1, diff, maxlength)
            )
            my_hashmap[i][diff + 5000] = maxHeight
            return maxHeight

        achievedHeight = use_rods(0, 0, sum(rods) // 2)
        #print(sum(rods), achievedHeight)
        return achievedHeight // 2


        # Test cases:
        # [1000,999,998,10,20,30,60]
        # [1,2,3,4,5,6]
        # [1,2]
        # [85,430,306,292,376,97,34,295,97,469,43,461,47,370,432,197,75,455,253,20]
        # [252,65,31,431,212,63,281,365,14,150,165,18,118,359,483,354,464,405,427,6]
        # [1,2,3,4,5,6,7,8,9,100,200,300,400,500,350,111,77,33,11]
        # [10,5,5,1000]
        # [71,272,7,327,401,315,320,240,115,470,390,258,448,82,338,178,70,26,259,300]
