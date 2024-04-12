# 42 - Trapping Rain Water
class Solution:
    def trap(self, height: List[int]) -> int:
        pointer1 = 0
        pointer2 = len(height) - 1

        previous_height = 0

        def subtr(i, new_height):
            subtr = min(height[i], new_height)
            return subtr


        full_amount = 0
        new_height = 0
        while pointer2 > pointer1:
            '''Check if their height is 
            higher that the already observed heights
            '''
            #print("pointer1", pointer1, "pointer2", pointer2)
            if height[pointer1] > previous_height and height[pointer2] > previous_height:
                new_height = min(height[pointer1], height[pointer2])
                theoretical_amount = (new_height - previous_height) * (pointer2 - pointer1 - 1)
                #print("theoretical_amount", theoretical_amount)

                full_amount += theoretical_amount
                #print("full_amount", full_amount)


            if height[pointer1] < height[pointer2]:
                pointer1 += 1
                if pointer1 < pointer2:
                    full_amount -= subtr(pointer1, new_height)

            elif height[pointer2] < height[pointer1]:
                pointer2 -= 1
                if pointer1 < pointer2:
                    full_amount -= subtr(pointer2, new_height)
            else:
                pointer1 += 1
                pointer2 -= 1
                if pointer1 <= pointer2:
                    full_amount -= subtr(pointer1, new_height)
                if pointer1 < pointer2:
                    full_amount -= subtr(pointer2, new_height)

            previous_height = new_height

        return full_amount
