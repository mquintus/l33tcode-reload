# 2028 - Find Missing Observations
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        curr_sum = sum(rolls)
        total_count = m+n
        missing_sum = mean * total_count - curr_sum
        avg_missing = missing_sum / n
        #print("avg_missing", avg_missing)
        if avg_missing < 1:
            return []
        if avg_missing > 6:
            return []
        smaller = missing_sum//n
        if missing_sum / n == smaller:
            return [smaller] * n
        smaller_sum = smaller * n
        missing_sum -= smaller_sum
        result = [smaller] * n
        result[-missing_sum:] = [smaller+1]*missing_sum
        return result
