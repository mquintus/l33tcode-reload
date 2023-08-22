class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        solution = ""
        while columnNumber > 0:
            columnNumber -= 1
            currentLetter = (columnNumber) % 26
            solution = chr(((ord("A") + ((currentLetter) % 26)) ))  + solution
            columnNumber //= 26
        return solution
