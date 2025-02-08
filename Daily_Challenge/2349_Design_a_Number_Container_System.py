# 2349 - Design a Number Container System
class NumberContainers:

    def __init__(self):
        self.number_to_position = {}
        self.position_to_number = {}

    def change(self, index: int, number: int) -> None:

        #print(self.number_to_position)
        #print(self.position_to_number)

        if number not in self.number_to_position:
            self.number_to_position[number] = []

        # insert
        #print("Insert",number,'at',index)
        if index not in self.position_to_number:
            self.position_to_number[index] = number
            self.number_to_position[number].append(index)
            self.number_to_position[number].sort()
            return

        # replace
        if index in self.position_to_number:
            oldnumber = self.position_to_number[index]
            #print("Replace",oldnumber,"With",number)
            if oldnumber == number:
                return

            if oldnumber != number:
                #print(self.number_to_position[oldnumber])
                #print("Delete index",index,"from being listed as pointing to",oldnumber)
                oldindex = bisect.bisect_left(self.number_to_position[oldnumber], index)
                #print("Delete from index", oldindex)
                del self.number_to_position[oldnumber][oldindex]
                self.number_to_position[number].append(index)
                self.number_to_position[number].sort()
                self.position_to_number[index] = number

    def find(self, number: int) -> int:
        #print("Find", number)
        #print(self.number_to_position)
        #print(self.position_to_number)
        if number not in self.number_to_position or len(self.number_to_position[number]) == 0:
            return -1

        #print("Found", number, "at", self.number_to_position[number][0])
        return self.number_to_position[number][0]
            
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
