# 1415 - The k-th Lexicographical String of All Happy Strings of Length n
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        counter = 0
        def appends(i,prev):
            nonlocal counter,k
            #print(i,prev)
            if i == n:
                counter += 1
                if counter == k:
                    return prev
                else:
                    return None
            for seq in 'abc':
                if seq != prev[-1]:
                    prev.append(seq)
                    res = appends(i+1, prev)
                    if res is not None:
                        return res
                    prev.pop()
                if counter == k:
                    return prev
            if counter == k:
                    returnprev
        result = appends(0,[""])
        if result == None:
            return ""
        return "".join(result[1:])

