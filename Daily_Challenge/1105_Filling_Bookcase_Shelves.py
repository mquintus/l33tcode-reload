# 1105 - Filling Bookcase Shelves
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        
        @cache
        def rec(i, prev_width, prev_height):
            nonlocal n
            nonlocal books
            nonlocal shelfWidth
        
            if i == n:
                return prev_height

            curr_width, curr_height = books[i]
            next_width = curr_width + prev_width
            if prev_width == 0 or (prev_height >= curr_height and not next_width > shelfWidth):
                new_row = float('inf')
            else:
                new_row = prev_height + rec(i, 0, 0)

            if next_width > shelfWidth:
                extend_row = float('inf')
            else:
                next_height = max(prev_height, curr_height)
                extend_row = rec(i+1, next_width, next_height)

            return min(extend_row, new_row)
        
        return rec(0,0,0)

        








