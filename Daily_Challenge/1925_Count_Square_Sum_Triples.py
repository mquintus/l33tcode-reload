# 1925 - Count Square Sum Triples
class Solution:
    def countTriples(self, n: int) -> int:
        squares = set()
        for i in range(n+1):
            squares.add(i**2)

        total = 0
        for i in range(1,n+1):
            for j in range(i+1, n+1):
                if i**2 + j**2 <= n**2:
                    if (i**2 + j**2) in squares:
                        #print(i, j)
                        total += 1
                        if i != j:
                            total += 1
                else:
                    break
        return total
