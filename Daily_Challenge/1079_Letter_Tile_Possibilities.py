# 1079 - Letter Tile Possibilities
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        inventory = Counter(tiles)
        
        def dfs():
            c = 0
            for letter, count in inventory.items():
                if count == 0: continue
                inventory[letter] -= 1
                c += 1
                c += dfs()
                inventory[letter] += 1
            return c

        return dfs()
