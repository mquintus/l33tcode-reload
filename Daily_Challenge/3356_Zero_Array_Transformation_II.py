# 3356 - Zero Array Transformation II
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if max(nums) == 0:
            return 0

        @cache
        def isPossible(k):
            #print("Testing k",k)
            dec = [[q[0], q[2]] for q in queries[:k]]
            dec.sort()
            inc = [[q[1], q[2] ]for q in queries[:k]]
            inc.sort()
            op = 0
            di = 0
            ii = 0
            for p, el in enumerate(nums):
                #print(di,dec[di], ii,inc[ii], op)
                while di < len(dec) and dec[di][0] <= p:
                    op += dec[di][1]
                    di += 1
                while ii < len(inc) and inc[ii][0] < p:
                    op -= inc[ii][1]
                    ii += 1
                #print(di, ii, op)
                #print((p, di,ii, op, el))
                if el > op: return False
            return True

        if not isPossible(len(queries)):
            return -1
        if isPossible(1):
            return 1

        start = 1
        end = len(queries)
        while start <= end:
            mid = (start+end)//2
            ip = isPossible(mid)
            #print(start,end,mid,ip,isPossible(mid-1))
            if ip:
                if not isPossible(mid-1):
                    return mid
                else:
                    end = mid 
            else:
                start = mid + 1
        return mid
