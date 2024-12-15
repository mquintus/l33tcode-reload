# 1792 - Maximum Average Pass Ratio
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        for c in classes:
            p, t = c
            r1 = p/t
            r2 = (p+1)/(t+1)
            c[:] = [r1-r2, t, p]
        heapq.heapify(classes)

        for i in range(extraStudents):
            #print(classes)
            r,t,p = classes[0]
            
            t += 1
            p += 1

            r1 = p/t
            r2 = (p+1)/(t+1)

            c = [r1-r2, t, p]
            heapq.heapreplace(classes, c)
        #print(classes)

        avg = 0
        for _, t, p in classes:
            avg += p/t
        return avg / len(classes)
