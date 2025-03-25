# 3394 - Check if Grid can be Cut into Sections
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        start_x = [x for x,_,_,_ in rectangles]
        start_y = [y for _,y,_,_ in rectangles]
        end_x = [x for _,_,x,_ in rectangles]
        end_y = [y for _,_,_,y in rectangles]

        for start, end in [(start_x, end_x), (start_y, end_y)]:
            num = 0
            cuts = 0
            start.sort()
            end.sort()
            i_e = 0
            i_s = 0
            while i_e < len(end) - 1:
                e = end[i_e]
                i_e += 1
                num -= 1
                while i_s < len(start) and start[i_s] < e:
                    num += 1
                    i_s += 1
                if num == 0:
                    cuts += 1
                if cuts > 1:
                    return True
        return False

                


