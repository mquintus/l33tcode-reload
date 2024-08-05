# 2053 - Kth Distinct String in an Array
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        n = len(arr)
        #once = set([chr(l) for l in range(ord('a'), ord('z')+1)])
        #twice = set([chr(l) for l in range(ord('a'), ord('z')+1)])
        #distinct = set([chr(l) for l in range(ord('a'), ord('z')+1)])
        once = set()
        twice = set()
        for letter in arr:
            if letter in once:
                twice.add(letter)
            else:
                once.add(letter)
        distinct = once - twice

        i = 0
        while i < n and k > 0:
            letter = arr[i]
            if letter in distinct:
                k -= 1
                if k == 0:
                    return letter
            i += 1
        return ""
