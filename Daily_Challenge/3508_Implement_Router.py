# 3508 - Implement Router
class Router:

    def __init__(self, memoryLimit: int):
        self.fifo = deque()
        self.fifo_per_dest = {}
        self.hashset = set()
        self.memoryLimit = memoryLimit

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        tup = (timestamp, source, destination)
        if tup in self.hashset:
            return False
        while len(self.hashset) >= self.memoryLimit:
            self.forwardPacket()
        self.hashset.add(tup)
        self.fifo.append(tup)
        if destination not in self.fifo_per_dest:
            self.fifo_per_dest[destination] = deque()
        self.fifo_per_dest[destination].append(tup)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.fifo:
            return []
        tup = self.fifo.popleft()
        dst = tup[2]
        self.fifo_per_dest[dst].popleft()
        self.hashset.remove(tup)
        return [tup[1], tup[2], tup[0]]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.fifo_per_dest or len(self.fifo_per_dest[destination]) == 0:
            return 0
        left = bisect.bisect_left(self.fifo_per_dest[destination], (startTime,-1,-1))
        right = bisect.bisect_right(self.fifo_per_dest[destination], (endTime,float('inf'),-1))
        return right-left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
