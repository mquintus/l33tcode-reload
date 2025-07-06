# 1865 - Finding Pairs With a Certain Sum
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.count1 = Counter(nums1)
        self.count2 = Counter(nums2)


    def add(self, index: int, val: int) -> None:
        oldval = self.nums2[index]
        self.count2[oldval] -= 1
        if self.count2[oldval] == 0:
            del self.count2[oldval]
        newval = oldval + val
        self.nums2[index] = newval
        if not newval in self.count2:
            self.count2[newval] = 0
        self.count2[newval] += 1

    def count(self, tot: int) -> int:
        answer = 0
        for val, freq1 in self.count1.items():
            target = tot - val
            if not target in self.count2:
                continue
            freq2 = self.count2[target]
            answer += freq1 * freq2

        return answer
            


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
