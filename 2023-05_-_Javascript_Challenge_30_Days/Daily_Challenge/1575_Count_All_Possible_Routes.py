import functools
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        '''
        A dynamic programming challenge
        '''
        @cache
        def solve(start: int, finish: int, fuel: int) -> int:
            paths = 0
            if start == finish:
                paths = 1

            for i, location in enumerate(locations):
                if i == start:
                    continue
                distance = abs(location - locations[start])
                if distance > fuel:
                    continue
                paths += solve(i, finish, fuel - distance)

            return paths
        return solve(start, finish, fuel) % (10**9 + 7)
