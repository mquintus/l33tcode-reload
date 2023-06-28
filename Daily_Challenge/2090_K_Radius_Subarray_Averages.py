class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        divisor = 2*k+1
        avgs = []

        running_sum = sum(nums[0:k*2]) 
        for i in range(0, len(nums)):
            if i < k:
                avgs.append(-1)
                continue
            elif i >= len(nums) - k:
                avgs.append(-1)
                continue
            else:
                running_sum += nums[i + k]
                running_avg = running_sum // divisor
                avgs.append(running_avg)
                running_sum -= nums[i-k] 

        return avgs

