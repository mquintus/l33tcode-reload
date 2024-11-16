# 3254 - Find the Power of K-Size Subarrays I
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        n = len(nums)
        result = []
        prev = nums[0]
        k -= 1
        conse = 1
        for i, el in enumerate(nums[1:]):
            if el == prev + 1:
                conse += 1
                #print(el, conse)
                if conse > k:
                    result.append(el)
            else:
                if i > n - k - 1:
                    break
                #print("conse",conse)
                if conse > k-1:
                    conse = min(n - k - len(result) - 1, k)
                    #print("conse",conse)
                result.extend([-1]*conse)
                conse = 1
            prev = el
            #print(el, result)
        #print(i, conse, el,n, "n - k - len(result)", n - k - len(result), "conse", conse)
        #if conse > 1 and conse < k: 
        #print(result)
        result.extend([-1]*max(n - k - len(result), 0))
        #print(result)
        return result

