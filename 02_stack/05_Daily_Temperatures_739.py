class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Let's iterate from the beginning.
        When the next element is bigger, write 1
        When the next element is smaller, delay write
            When the next element is smaller, delay write
                When the next element is smaller, delay write
                    When the next element is bigger, 
                    write 1
                Write 2
            Write 3


        1   1
        2   1
        3   wait
        2   wait
        1   1
        2   1 -> solve(2)
        3   1 -> solve(3)
        4   0

        So if we put all unsolved elements into a stack,
        we can always compare to the top element of the stack,        
        because the stack will be a min stack.

        Pseudo code:
        curr_day = 0, temp = 73, stack = [], next_day = 1, wait = 1
        curr_day = 1, temp = 74, stack = [], next_day = 2, wait = 1
        curr_day = 2, temp = 75, stack = [], next_day = 3, wait = ?
        curr_day = 3, temp = 71, stack = [(2, 75)], next_day = 4, wait = ?
        curr_day = 4, temp = 69, stack = [(2, 75), (3, 71)], next_day = 5, wait = 1
        curr_day = 5, temp = 72
        while stack.top().temp < curr_day.temp:
             backtrack = stack.pop()
             results[backtrack.day] = curr_day - backtrack.day
        '''
        class Day_Temp:
            def __init__(self, day, temp):
                self.day = day
                self.temp = temp
            #def __str__(self):
            #    return [self.day, self.temp].__str__()
            #def __repr__(self):
            #    return self.__str__()


        myStack = []
        results = []

        for curr_day, temp in enumerate(temperatures):
            #print(myStack)
            next_day = curr_day + 1
            if next_day >= len(temperatures):
                results.append(0)
                break
            
            if temperatures[next_day] > temp:
                results.append(1)
            
            while len(myStack) > 0 and myStack[-1].temp < temperatures[next_day]:
                old_day = myStack.pop().day
                wait_length = next_day - old_day
                results[old_day] = wait_length
            
            if temperatures[next_day] <= temp:
                myStack.append(Day_Temp(curr_day, temp))
                results.append(0)

        return results
