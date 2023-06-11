class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [0 for i in range(length)]
        self.snaps = [{0: 0} for i in range(length)]
        self.snap_ctr = 0
        self.changed = [True for i in range(length)]

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val
        self.changed[index] = True
        self.snaps[index][self.snap_ctr] = val

    def snap(self) -> int:
        self.snap_ctr += 1
        return self.snap_ctr - 1

    def get(self, index: int, snap_id: int) -> int:
        while not snap_id in self.snaps[index]:
            snap_id -= 1
        return self.snaps[index][snap_id]

        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
