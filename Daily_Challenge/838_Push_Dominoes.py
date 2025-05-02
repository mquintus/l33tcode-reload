# 838 - Push Dominoes
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        result = []
        force = 0
        waiting = 0
        for el in dominoes:
            if force == 0 and el == '.':
                waiting += 1
                continue
            if force == 0 and el == 'R':
                result.extend(['.']*waiting)
                waiting = 1
                force = 1
                continue
            if force == 0 and el == 'L':
                result.extend(['L']*waiting)
                result.append('L')
                waiting = 0
                continue
            if force == 1 and el == 'R':
                result.extend(['R']*waiting)
                waiting = 1
                continue
            if force == 1 and el == '.':
                waiting += 1
                continue
            if force == 1 and el == 'L':
                waiting += 1
                result.extend(['R']*(waiting//2))
                if waiting %2 == 1:
                    result.append('.')
                result.extend(['L']*(waiting//2))
                force = 0
                waiting = 0
                continue
        if force == 1:
            result.extend(['R']*(waiting))
        if force == 0:
            result.extend(['.']*(waiting))


        return "".join(result)
            
                
