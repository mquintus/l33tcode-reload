# 1331 - Rank Transform of an Array
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return []
        arr_tuple = [[arr[i], i] for i in range(len(arr))]
        arr_tuple.sort()
        arr_tuple[0][0] = 1
        arr.sort()
        for i in range(1, len(arr)):
            if arr_tuple[i][0] == arr[i-1]:
                arr_tuple[i][0] = arr_tuple[i-1][0]
            else:
                arr_tuple[i][0] = arr_tuple[i-1][0] + 1
        
        res_tuple = [[pos, rank] for rank, pos in arr_tuple]
        res_tuple.sort()
        return [rank for pos, rank in res_tuple]
