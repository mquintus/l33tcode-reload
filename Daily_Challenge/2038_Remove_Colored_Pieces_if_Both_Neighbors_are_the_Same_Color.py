# 2038 - Remove Colored Pieces if Both Neighbors are the Same Color
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice_wins = 0
        i = 0
        while i < len(colors) - 2:
            while colors[i:i+3] == 'AAA':
                alice_wins += 1
                i += 1
            while colors[i:i+3] == 'BBB':
                alice_wins -= 1
                i += 1
            i += 1

        return alice_wins > 0



        
