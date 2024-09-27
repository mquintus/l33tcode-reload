# 731 - My Calendar II
class MyCalendarTwo:

    def __init__(self):
        self.moments = []
        #self.run = 0

    def book(self, start: int, end: int) -> bool:
        #print(self.run, "BOOK", start,end)
        #self.run += 1
        #print(self.moments)
        prev, precount = -1,0
        for time, count in self.moments:
            if time >= start and time < end and count == 2:
                #print("Overlap. Abort!")
                return False
            if start > prev and start < time and precount == 2:
                #print("Overlap! Abort!")
                return False
            prev, precount = time, count
            if end < time:
                break

        if len(self.moments) == 0:
            self.moments.append((start, 1))
            self.moments.append((end, 0))
            #print(self.moments)
            return True

        prev = -1 
        prevcount = 0
        addstart = False
        addend = False
        i = 0
        while i < len(self.moments):
            time, count = self.moments[i]

            if time > start and prev < start:
                self.moments.insert(i, (start, prevcount + 1))
                addstart = True
                if time > end:
                    i += 1
                    self.moments.insert(i, (end, prevcount))
                    addend = True
                    break
            elif time >= start and time < end:
                self.moments[i] = (time, count + 1)
                addstart = True
            elif time > end:
                self.moments.insert(i, (end, prevcount))
                addend = True
                break

            prev = time
            prevcount = count

            i += 1
        if not addstart:
            #print("Not added start")
            self.moments.append((start, prevcount + 1))
        if not addend:
            #print("Not added end")
            self.moments.append((end, prevcount))

        #print(self.moments)
        return True
            





# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
