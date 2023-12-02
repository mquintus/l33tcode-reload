# 1160 - Find Words That Can Be Formed by Characters
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        myHashtable = {}
        for c in chars:
            if c not in myHashtable:
                myHashtable[c] = 0
            myHashtable[c] += 1

        matching_count = 0

        for word in words:
            local_count = {}
            local_length = 0
            for c in word:
                if c not in local_count:
                    local_count[c] = 0
                local_count[c] += 1
                if c not in myHashtable or local_count[c] > myHashtable[c]:
                    break
                local_length += 1
            else:
                matching_count += local_length
        return matching_count
