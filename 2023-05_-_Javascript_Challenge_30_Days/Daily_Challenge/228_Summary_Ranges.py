class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        start = None
        result = []
        for i in nums:
            if start is None:
                prev = i
                start = i
                end = i
                continue
            if i == prev + 1:
                end = i
                prev = i
                continue
            if i > prev + 1:
                if start == end:
                    result.append(str(prev))
                if start < end:
                    result.append(f"{start}->{end}")
                start = i
                end = i
                prev = i
        if start == end:
            result.append(str(prev))
        if start < end:
            result.append(f"{start}->{end}")
            
        return result

