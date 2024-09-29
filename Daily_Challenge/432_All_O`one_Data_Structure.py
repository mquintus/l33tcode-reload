# 432 - All O`one Data Structure
class Node():
    def __init__(self, value, before, after, count):
        self.value = value
        self.before = before
        self.after = after
        self.count = count

class AllOne:
    def __init__(self):
        self.hashmap = {}
        self.first = None
        self.last = None

    def inc(self, key: str) -> None:
        if key not in self.hashmap:
            node = Node(key, None, self.first, 0)
            if self.first is not None:
                self.first.before = node
            self.first = node
            self.hashmap[key] = node

        node = self.hashmap[key]
        node.count += 1
        #print(key,node.count)
        while node.after is not None and node.after.count < node.count:
            if self.first == node and node is not None:
                self.first = node.after

            prev = node.before
            nex = node.after

            nexnex = None
            if nex is not None:
                nexnex = nex.after

            if prev is not None:
                prev.after = nex

            if nex is not None:
                nex.before = prev
            
            if nex is not None:
                nex.after = node
            node.before = nex

            node.after = nexnex
            if nexnex is not None:
                nexnex.before = node

        if node.after is None:
            self.last = node

        #print("Increased",key,"to",node.count)
        #somenode = self.first
        #while somenode is not None:
        #    print(somenode.value, end=',')
        #    somenode = somenode.after
        #print("Last:",self.last.value)


    def dec(self, key: str) -> None:
        if key not in self.hashmap:
            return

        node = self.hashmap[key]
        node.count -= 1
        if node.count == 0:
            prev = node.before
            nex = node.after
            if nex is not None:
                nex.before = prev
            if prev is not None:
                prev.after = nex
            if node == self.first:
                self.first = nex
            if node == self.last:
                self.last = prev
            del self.hashmap[key]
            return

        while node.before is not None and node.before.count > node.count:
            prev = node.before
            nex = node.after
            prevprev = None
            if prev is not None:
                prevprev = prev.before

            if prev is not None:
                prev.after = nex

            if nex is not None:
                nex.before = prev
            
            if prev is not None:
                prev.before = node
            node.after = prev

            node.before = prevprev
            if prevprev is not None:
                prevprev.after = node
            
            if self.last == node:
                self.last = prev

        if node.before is None:
            self.first = node


        #print("Decreased",key,"to",node.count)
        #somenode = self.first
        #while somenode is not None:
        #    print(somenode.value, end=',')
        #    somenode = somenode.after
        #if self.last is not None:
        #    print()
        #    print("Last:",self.last.value)
        #else:
        #    print()
        #    print("No Last Node Found")


    def getMaxKey(self) -> str:
        if self.last is None:
            return ""
        return self.last.value

    def getMinKey(self) -> str:
        if self.first is None:
            return ""
        return self.first.value
    

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
