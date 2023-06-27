class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # vertical binary search
        start = 0
        end = len(matrix)
        
        while start <= end - 1:
            mid = (end - start) //2 + start
            first_el = matrix[mid][0]
            if first_el > target:
                end = mid
                continue
            last_el = matrix[mid][-1]
            if last_el < target:
                start = mid + 1
                continue
            break

        #horizontal
        h_start = 0
        h_end = len(matrix[mid])

        while h_start <= h_end - 1:
            h_mid = (h_end - h_start ) //2 + h_start
            h_el = matrix[mid][h_mid]
            if h_el == target:
                return True
            if h_el < target:
                h_start = h_mid + 1
                continue
            if h_el > target:
                h_end = h_mid
                continue
        return False


