# 1733 - Minimum Number of People to Teach
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = [set(l) for l in languages]
        used_languages = set()
        for lset in languages:
            used_languages |= lset
        def have_common_language(p1,p2):
            for l in languages[p1-1]:
                if l in languages[p2-1]:
                    return True
            return False

        unresolved = set()
        for edge in friendships:
            p1, p2 = edge
            if not have_common_language(p1,p2):
                unresolved.add(p1)
                unresolved.add(p2)

        mincount = float('inf')
        for l in used_languages:
            count = 0
            for u in unresolved:
                if l not in languages[u-1]:
                    count += 1
            mincount = min(mincount, count)
        
        return mincount


