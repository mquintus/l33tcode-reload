# 1482 - Minimum Number of Days to Make m Bouquets
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1
        if m * k == n:
            return max(bloomDay)
        possibleBloomDays = sorted(list(set(bloomDay)))
        n2 = len(possibleBloomDays)
        def BouquetsPossible(day):
            if day == -1:
                return False
            nonlocal bloomDay
            nonlocal n
            nonlocal m
            nonlocal k

            success = False

            p0 = 0
            p1 = 0
            numBouquets = 0
            while p0 < n and p1 < n:
                while bloomDay[p0] > day:
                    #print("p0",p0,"is not yet blooming")
                    p0 += 1
                    p1 = p0
                    if p0 >= n:
                        break
                if p0 >= n:
                    #print("Timeout")
                    break
                #print("p0",p0,"is blooming now")
                while p1 < n:
                    if p1 == n:
                         break
                    if bloomDay[p1] > day:
                        #print("p1",p1,"is not yet blooming")
                        p0 = p1
                        break
                    elif p1 - p0 + 1 == k:
                        #print("enough flowers", p0, p1, "finished bouquets",numBouquets)
                        numBouquets += 1
                        if numBouquets == m:
                            success = True
                        p0 = p1 + 1
                        break
                    p1 += 1
                if p1 == n:
                    break
            return success


        start = 0
        end = n2
        possible = -1
        while start < end:
            day_index = start + (end-start) // 2
            day = possibleBloomDays[day_index]
            #print("BS", day_index, day)
            if BouquetsPossible(day):
                #print('yes -----------------')
                #return 1
                possible = day
                if not BouquetsPossible(day - 1):
                    return day
                end = day_index
            else:
                #print('no -------------------')
                #return 2
                start = day_index + 1
        return -1
                

