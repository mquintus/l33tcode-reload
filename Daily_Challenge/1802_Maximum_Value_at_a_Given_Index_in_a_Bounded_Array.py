class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left = 1
        right = maxSum+1

        def getSum(mid):
            #print("If index",index,"has a value of",mid,"...")
            myIndex = index
            if myIndex == 0:
                leftHalf = mid
            elif myIndex == mid-1:
                leftHalf = (mid*(mid+1))//2
            elif myIndex > mid-1:
                leftHalf = (mid*(mid+1))//2 + (myIndex-mid+1)
            elif myIndex < mid-1:
                missing = mid-myIndex-1
                leftHalf = (mid*(mid+1))//2 - (missing*(missing+1))//2
                #print("Left half: ", (mid*(mid+1))//2, "-", (missing*(missing+1))//2, "=", leftHalf)
            #print("n",n,"index",myIndex, "Left half: ",leftHalf)
            rightHalf = leftHalf

            leftHalf = 0
            myIndex = n - 2 - myIndex
            #print("index from the other side", myIndex)
            if index < n-1 and myIndex <= n-1:
                mid -= 1
                if mid <= 1:
                    leftHalf = 1 * (myIndex +1)
                elif myIndex == 0:
                    leftHalf = mid
                elif myIndex == mid-1:
                    leftHalf = (mid*(mid+1))//2
                elif myIndex > mid-1:
                    leftHalf = (mid*(mid+1))//2 + (myIndex-mid+1)
                elif myIndex < mid-1:
                    missing = mid-myIndex-1
                    leftHalf = (mid*(mid+1))//2 - (missing*(missing+1))//2

            #print("If index from the right",myIndex,"has a value of",mid,"the array in total would have a sum of leftHalf + rightHalf",rightHalf, "+", leftHalf, "=", leftHalf + rightHalf)
            return leftHalf + rightHalf

        while left < right:
            mid = (left+right)//2
            #print('---------------')
            #print("Trying",mid,"for index",index)

            totalSum = getSum(mid)
            if totalSum > maxSum:
                right = mid
            elif totalSum <= maxSum:
                if getSum(mid+1) > maxSum:
                    return mid
                else:
                    left = mid + 1

        return mid

        
        
