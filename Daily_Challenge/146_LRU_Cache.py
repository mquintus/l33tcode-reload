class DoubleLinkedListElement:
    next = None
    prev = None
    val = None
    key = None

    def __init__(self, key: int, val: int):
        self.val = val
        self.key = key

class LRUCache:
    def make_el_first(self, key):
        if self.lru_head.key == key:
            return

        pre_tail = self.lru_tail.prev
        second = self.lru_head

        # get element from store
        new_el = self.store[key]

        # connect the prv and nxt element from el
        if new_el.prev is not None:
            new_el.prev.next = new_el.next
        if new_el.next is not None:
            new_el.next.prev = new_el.prev

        # List head
        self.lru_head = new_el
        self.lru_head.next = second
        self.lru_head.next.prev = self.lru_head
        self.lru_head.prev = None

        # List tail
        if self.lru_tail.key == key:
            if pre_tail is not None:
                self.lru_tail = pre_tail
                self.lru_tail.next = None

    def __init__(self, capacity: int):
        self.store = {}
        self.lru_head = None
        self.lru_tail = None
        self.remaining_capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        
        self.make_el_first(key)

        return self.lru_head.val

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.make_el_first(key)
            self.store[key].val = value
            return

        if self.remaining_capacity == 0:
            tail_el = self.lru_tail
            if self.lru_tail.prev is not None:
                self.lru_tail = self.lru_tail.prev
            del self.store[tail_el.key]
            if tail_el.key == self.lru_head.key:
                self.lru_head = None

        el = DoubleLinkedListElement(key, value)
        
        if self.lru_head is None:
            self.lru_head = el
            self.lru_tail = self.lru_head

        
        self.store[key] = el
        self.make_el_first(key)

        if self.lru_tail is None:
            self.lru_tail = el
            self.lru_tail.prev = self.lru_head

        if self.remaining_capacity > 0:
            self.remaining_capacity -= 1

    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
