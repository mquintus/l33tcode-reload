# 1903 - Largest Odd Number in String
class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Odd numbers are determined by the last digit.
        # Therefore, the latest non-even digit is the smallest digit of the number
        # The most efficient way
        # is to parse the number from the back
        # looking for an odd number
        # and returning everything left from the first found odd digit.

        for pointer in range(len(num)-1, -1, -1):
            if int(num[pointer]) % 2 == 1:
                pointer += 1
                break
        return num[:pointer]
