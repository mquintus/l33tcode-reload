class Solution:
    def canCross(self, stones: List[int]) -> bool:
        binary_stone = 0
        # Actually, this is a gaussian sequence so 
        # no reachable stone can be farther away than n(n+1) / 2
        # with n is at max 2000 so roughly n ** 2
        max_distance_reachable = 2000 * 2000
        # This preprocessing step failed during testcase 51.
        # Therefore I added the check.
        reachable_speed = 1
        reachable_distance = 1
        for stone in stones:
            if stone > reachable_distance:
                return False
            reachable_speed += 1
            reachable_distance += reachable_speed
            binary_stone |= (1 << stone)
        
        # after weeding out the invalid testcases 
        # and creating the binary dp array
        # let's get started with the actual algorithm
        dp = [0] * 2002 
        def solve(i, l):
            j = stones.index(i)
            if j == len(stones) - 1:
                return True

            been_here = dp[j]
            if (been_here & (1 << l)) > 0:
                return False
            dp[j] |= (1 << l)

            
            for length in [l - 1, l + 1, l]:
                next_pos = i + length
                if next_pos <= 0 or length <= 0:
                    continue
                next_pos_bin = (1 << next_pos)
                if binary_stone & next_pos_bin > 0:
                    success = solve(next_pos, length)
                    if success:
                        return True
            return False

        return solve(0,0)
