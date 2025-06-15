# 1432 - Max Difference You Can Get From Changing an Integer
class Solution:
    def maxDiff(self, num: int) -> int:
        # IF THE NUMBER IS ONLY ONE DIGIT, RETURN 8
        strnum = str(num)
        if len(strnum) == 1:
            return 8

        # SHOULD WE REPLACE WITH 0 OR WITH 1???
        # THIS IS ONLY DECIDED BY THE QUESTION WHETHER WE GET A LEADING 0
        # TO FIND WHETHER WE GET A LEADING 0
        # THE RULES ARE
        # 
        # IF THE NUMBER STARTS WITH "1" THEN WE CAN REPLACE THE NEXT NUMBER WITH "0"
        # ELSE WE REPLACE THE FIRST NUMBER THAT IS BIGGER THAT 1 WITH "1"
        #
        # 202 -> 101
        # 220 -> 110
        # 999 -> 111
        # 123 -> 103 !!!!!!!!!!
        # 101 -> 101
        # 1001 -> 1001
        
        useone = "1"
        if strnum[0] == "1":
            useone = "0"

        #print(useone)

        highest = []
        lowest = []
        reph = -1
        repm = -1
        for i, el in enumerate(strnum):
            #print("....", i, el)
            if int(el) < 9 and reph == -1:
                reph = el
            h = el
            if el == reph:
                h = "9"
            highest.append(h)
            
            m = el
            if repm == -1 and int(el) > int(useone) and (int(el) > 1 or useone == "1"):
                repm = el
                #print("REPLACE",repm,"with",useone)
            if el == repm:
                m = useone
            lowest.append(m)
        highest = int("".join(highest))
        lowest = int("".join(lowest))
        #print(highest, lowest)
        return highest - lowest
