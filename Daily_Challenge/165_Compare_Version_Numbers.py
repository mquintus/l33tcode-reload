# 165 - Compare Version Numbers
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(a) for a in version1.split('.')]
        v2 = [int(a) for a in version2.split('.')]
        while len(v1) > 1 and v1[-1] == 0:
            v1.pop()
        while len(v2) > 1 and v2[-1] == 0:
            v2.pop()
        if v1 == v2:
            return 0
        if v1 < v2:
            return -1
        return 1
