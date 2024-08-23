# 592 - Fraction Addition and Subtraction
class Solution:
    def fractionAddition(self, expression: str) -> str:
        fracStack = []
        numerStack = []
        p = 0
        n = len(expression)
        largestFractor = 1
        while p < n:
            if expression[p] == '+':
                p += 1
            elif expression[p] == '-':
                pass
            #else:
            #    print("FAIL at", p, expression[p])
            #    return ""

            divisor = expression[p:].find('/')
            numerator = int(expression[p:p+divisor])
            numerStack.append(numerator)
            #print("numerStack, divisor", numerStack, divisor)

            p += divisor + 1
            nextPlus = expression[p:].find('+')
            nextMinus = expression[p:].find('-')
            if nextPlus == -1:
                nextAddition = nextMinus
            elif nextMinus == -1:
                nextAddition = nextPlus
            else:
                nextAddition = min(nextPlus, nextMinus)
            if nextAddition == -1:
                nextAddition = n

            fractor = int(expression[p:p+nextAddition])
            fracStack.append(fractor)
            p += nextAddition
            #print(fracStack)

            gcd = math.gcd(fractor, largestFractor)
            largestFractor = abs(largestFractor*fractor) // math.gcd(largestFractor, fractor)

        numerSum = 0
        for i in range(len(fracStack)):
            num = numerStack[i]
            frac = 1
            if fracStack[i] < largestFractor: 
                mult = largestFractor // fracStack[i]
                #print("mult", mult)
                num *= (mult)
            numerSum += num
            #print("Sum up", num, numerSum)
        #print("SummedUp", numerSum)
        gcd = math.gcd(numerSum, largestFractor)
        #print("gcd", gcd)
        numerSum //= gcd
        largestFractor //= gcd
        if numerSum == 0:
            largestFractor = 1
        return f"{numerSum}/{largestFractor}"


