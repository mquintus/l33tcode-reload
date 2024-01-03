# 2125 - Number of Laser Beams in a Bank
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        '''
        Intuition:
        Count 1s
        Drop each row with only zeros
        Pairwise multiply x and y (row i and row j)
        '''
        all_lasers = 0
        current_lasers = 0
        for row in bank:
            next_lasers = row.count('1')
            if next_lasers == 0:
                continue
            all_lasers += current_lasers * next_lasers
            current_lasers = next_lasers
        return all_lasers
