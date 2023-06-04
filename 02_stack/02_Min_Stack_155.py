class MinStack:
    '''
    Operations on a stack are simple and can be done in O(1)
    How to track the smallest element?
    Tracking only the smallest element is not enough, because 
    if it gets popped, we'd need a reference to the second smallest element.
    
    At first, it sounds like a linked list problem: When a smaller element
    is added, the smaller element gets a link a the less-smaller element
    and so if popped, we know about this.
    Problem: If we insert a bigger element, this logic isn't triggered, but at
    some point, it might become the smallest element?
    Not true! Since we are working on a stack, the bigger element will get popped
    *before* the smaller element.

Initial state:
+---+
| T |
+---+
Push (2):
+--------+---+
| 2,None | T |
+--------+---+
Smallest() : min(2,None) = 2
Push (1):
+-----+--------+---+
| 1,2 | 2,None | T |
+-----+--------+---+
Smallest() : min(1,2) = 1
Push (5):
+-----+-----+--------+---+
| 5,1 | 1,2 | 2,None | T |
+-----+-----+--------+---+
Smallest() : min(5,1) = 1

Pop() reverts to the previous state.
    '''

    def __init__(self):
        self.stack = []
            
    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            prevMin = None
        else:
            prevMin = self.getMin()
        self.stack.append([val, prevMin])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        prevEl = self.stack[-1]
        if prevEl[1] is None:
            return prevEl[0] 
        else:
            return min(prevEl)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
