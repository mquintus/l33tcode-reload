# 1291 - Sequential Digits
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low_array = [[123,2],[1234,3],[12345,4],[123456,5],[1234567,6],[12345678,7],[123456789,8]]

        min_length = 9
        max_length = 9
        for i, j in low_array:
            if low < i:
                min_length = j
                break
        for i, j in low_array:
            if high < i:
                max_length = j
                break
        
        things = "123456789"
        output = []
        n = 9
        for j in range(min_length, max_length+1):
            for i in range(9 - j + 1):
                result = int(things[i:i+j])
                #print(result)
                if result < low or result > high:
                    continue
                output.append(result)
        
        return output
