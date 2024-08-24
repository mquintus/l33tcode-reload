# 564 - Find the Closest Palindrome
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        num = n
        n = len(num)

        distance = float('inf')
        bestcurrnum = ""

        def ispalindrome(a):
            return a == a[::-1]
        def getdistance(a,b):
            return abs(int(a)-int(b))
        def check(currnum):
            #print("Check",currnum)
            nonlocal distance
            nonlocal bestcurrnum
            if len(currnum) == 0:
                return
            if currnum != num:
                gd = getdistance(currnum,num)
                #print("getdistance",gd)
                if gd < distance or (gd == distance and int(bestcurrnum)>int(currnum)):
                    distance = gd
                    bestcurrnum = currnum

        onlynine = "9" * (n-1)
        check(onlynine)
        oneoone = "1" + "0" * (n-1) + "1"
        #print(oneoone)
        check(oneoone)

        for currnum in [num, "1"+num, num[1:], str(int(num[0])-1)+num[1:]]:
            while len(currnum) > 0 and currnum[0] == "0":
                currnum = currnum[1:]
                if len(currnum) == 0:
                    break
            if len(currnum) == 0:
                continue
            #print(currnum)
            # normalize
            cn = len(currnum)
            middle = cn % 2
            currnum = currnum[:cn//2+middle] + currnum[:cn//2][::-1]
            
            check(currnum)
            for digit in range((cn+1)//2):
                first = currnum[:cn//2-digit]
                last =  currnum[:cn//2-digit][::-1]
                #print("first", first, "last",last)
                for direction in range(-9,9):
                    for drange in [digit, digit+1]:
                        something = ""
                        for d in range(drange):
                            #print("digit,direction,d,sustitute",digit,direction,d,int(currnum[:cn//2-digit+1]))
                            something += str((int(currnum[:cn//2-digit+1]) + direction) % 10)
                        #print("first", first, "something",something, "last",last)
                        nextcurrnum = first + something + last
                        check(nextcurrnum)

        return bestcurrnum
