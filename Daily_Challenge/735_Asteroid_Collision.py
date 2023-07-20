class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if len(stack) == 0:
                stack.append(a)
            elif stack[-1] < 0:
                stack.append(a)
            else:
                if a > 0 and stack[-1] > 0:
                    stack.append(a)
                    continue

                add = True
                while len(stack) > 0 and a < 0 and stack[-1] > 0:
                    if -a > stack[-1]:
                        stack.pop()
                        continue
                    elif -a == stack[-1]:
                        stack.pop()
                        add = False
                        break
                    else:
                        add = False
                        break
                if add:
                    stack.append(a)

        return stack
