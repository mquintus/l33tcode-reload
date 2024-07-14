# 726 - Number of Atoms
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        counts = {}
        upperletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lowerletters = upperletters.lower()
        numbers = '0123456789'
        n = len(formula)

        def getNumber(i):
            nonlocal n
            nonlocal formula
            nonlocal numbers
            currnum = ""
            while i < n and formula[i] in numbers:
                currnum += formula[i]
                i += 1
            if currnum == "":
                currnum = 1
            else:
                currnum = int(currnum)
            return currnum, i


        def getElemCount(i):
            nonlocal n
            nonlocal formula
            nonlocal upperletters
            nonlocal lowerletters
            nonlocal numbers

            counts = {}
            if formula[i] in upperletters:
                currel = formula[i]
                currnum = 0
                i += 1
                while i < n and formula[i] in lowerletters:
                    currel += formula[i]
                    i += 1
                
                currnum, i = getNumber(i)
                if currel not in counts:
                    counts[currel] = 0
                counts[currel] += currnum
            return counts, i


        def addCounts(counts, counts_rec, multiplier):
            for k,v in counts_rec.items():
                if k not in counts:
                    counts[k] = 0
                counts[k] += multiplier * v
            return counts

        def recursive(i):
            nonlocal n
            nonlocal formula
            nonlocal upperletters
            nonlocal lowerletters
            nonlocal numbers
            #print(formula[i:])
            counts = {}
            while i < n and formula[i] != ')':
                if formula[i] == '(':
                    counts_rec, i = recursive(i+1)
                    assert formula[i] == ')', f"{i},{formula[i]}"
                    i += 1
                    multiplier, i = getNumber(i)
                    #print("multiplier", multiplier)
                    assert i == n or (formula[i] in upperletters) or (formula[i] == '(') or (formula[i] == ')'), f"{i},{formula[i]}"
                    counts = addCounts(counts, counts_rec, multiplier) 
                else:
                    old_i = i
                    count_add, i = getElemCount(i)
                    counts = addCounts(counts, count_add, 1)
                    assert i > old_i
            return counts,i
        
        retval = ""
        counter, i = recursive(0)
        assert i == n
        #print(counter)
        elems = sorted(list(counter.keys()))
        for elem in elems:
            count = counter[elem]
            retval += elem 
            if count > 1:
                retval += count.__str__()
        return retval
