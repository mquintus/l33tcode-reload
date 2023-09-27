# 880 - Decoded String at Index
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        #print('-------------------')
        def solve_add(k, i, length):
            #print(f"solve_add({k}, {i}, {length})")
            # First case: We've found a letter.
            if ord(s[i]) > 90:
                start = i
                newlength = length
                while ord(s[i]) > 90:
                    #print("Add s[i]", s[i])
                    newlength += 1
                    #print("newlength, k", newlength, k)
                    if newlength - 1 == k:
                        return -1, s[i]
                    i += 1
                newindex, char = solve_multiply(k, i, newlength)
                if char != '':
                    return -1, char
                p = (start + (newindex - length))
                #print("ADD: Backtracking", newindex)
                #print("start + (newindex - length)", start, newindex, length, p)
                if newindex >= length and p < len(s):
                    #print("ADD: Found char at ", p, s[p])
                    return -1, s[p]
                return newindex, ''

        def solve_multiply(k, i, length) -> List[str]:
            #print(f"solve_multiply({k}, {i}, {length})")
            # found an integer
            multiplier = 1
            while ord(s[i]) < 90:
                multiplier *= int(s[i])
                newlength = length * multiplier
                if newlength > k:
                    realindex = k % length
                    #print("MULT: Found index", realindex)
                    return realindex, ''
                i += 1
            new_k, char = solve_add(k, i, newlength)
            if char == '':
                #print("MULT: Backtracking for", new_k, "Newlength", newlength, "Oldlength", length)
                return new_k % (length), ''
            else:
                #print("MULT: Passing through", char)
                return -1, char
        return solve_add(k - 1, 0, 0)[1]

