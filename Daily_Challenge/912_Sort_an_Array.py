# 912 - Sort an Array
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def twoPointer(start1, end1, start2, end2):
            nonlocal nums
            temp = []
            #print(start1,end1,start2, end2)
            p1 = start1
            p2 = start2
            i = nums[p1]
            j = nums[p2]
            while p1 < end1 and p2 < end2:
                i = nums[p1]
                j = nums[p2]
                if i <= j:
                    temp.append(i)
                    p1+=1
                if i >= j:
                    temp.append(j)
                    p2+=1
            if p1 == end1:
                temp.extend(nums[p2:end2])
            else:
                temp.extend(nums[p1:end1])
            #print(temp)
            nums[start1:end2] = temp

        def mergeSort(start, end):
            mid = (start + end) // 2
            if end <= start + 1:
                return
            mergeSort(start, mid)
            #print(nums)
            mergeSort(mid, end)
            #print(nums)
            twoPointer(start, mid, mid, end)
            #print(nums)
            return

        mergeSort(0, len(nums))
        return nums
