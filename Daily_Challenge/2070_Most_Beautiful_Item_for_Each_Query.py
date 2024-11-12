# 2070 - Most Beautiful Item for Each Query
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        beauty = 0

        for position, (price, curr_beauty) in enumerate(items):
            beauty = max(curr_beauty, beauty)
            items[position][1] = beauty

        #print(items)

        beauties = [0] * len(queries)
        queries = sorted(zip(queries, range(len(queries))))
        curr_item_index = 0
        curr_price = items[curr_item_index][0]
        for q,p in queries:
            #print(q,p,curr_price,curr_item_index)
            while curr_price <= q and curr_item_index < len(items):
                curr_item_index += 1
                if curr_item_index == len(items): break
                curr_price = items[curr_item_index][0]
            beauty = 0
            if curr_item_index > 0:
                beauty = items[curr_item_index-1][1]
            beauties[p] = beauty
        return beauties

