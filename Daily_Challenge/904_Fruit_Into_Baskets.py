# 904 - Fruit Into Baskets
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) < 3:
            return len(fruits)
        left = 0
        right = 1
        counter = {
           fruits[left]: 1 
        }
        distinct = 1
        if fruits[right] not in counter:
            counter[fruits[right]] = 0 
            distinct = 2
        counter[fruits[right]] += 1

        
        best = 2
        for right in range(2, len(fruits)):
            el = fruits[right]
            if el not in counter:
                counter[el] = 0
            if counter[el] > 0:
                counter[el] += 1
                length = right - left + 1
                best = max(best, length)
                continue

            while distinct == 2:
                to_remove = fruits[left]
                left += 1
                counter[to_remove] -= 1
                if counter[to_remove] == 0:
                    distinct = 1


            length = right - left + 1
            best = max(best, length)

            distinct = 2
            counter[el] += 1
        return best

