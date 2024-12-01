# 1346 - Check If N and Its Double Exist
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        pos = [False] * 3002
        neg = [False] * 3002
        for el in arr:
            scope = neg
            if abs(el) == el:
                scope = pos
            el = abs(el)
            try:

                if scope[el*2] == True:
                    return True
                if el % 2 == 0 and scope[el//2] == True:
                    return True
            except:
                pass
            scope[el] = True

        return False
