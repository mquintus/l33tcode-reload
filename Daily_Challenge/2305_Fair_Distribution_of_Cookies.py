class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        '''
        Max. 8 bags of cookies means that we can do backtracking through all of them.
        '''

        '''
        Edgecase 1: 
        If the number of children and the number of cookie (bags) is identical,
        just give each child one bag.
        '''
        if k == len(cookies):
            return max(cookies)

        def solve(children, i):
            '''
            Edgecase 2:
            If only one cookie is left, give it to the child with the lowest amount of cookies.
            Because the decision cannot affect later rounds (it is the last round).
            '''
            if i == len(cookies) - 1:
                poorest_child = 0
                poorest_child_cookies = children[0]
                for e, c in enumerate(children):
                    if c < poorest_child_cookies:
                        poorest_child_cookies = c
                        poorest_child = e
                children[poorest_child] += cookies[i]
                return max(children)

            '''
            Of all solutions, find the minimal one.
            '''
            u = 9999999999999
            for e, c in enumerate(children):
                '''
                e is the id of the child.
                i is the id of the cookie.
                It doesn't make sense to try giving the first cookie to any other child than
                the first child, because the outcome would be mirrored.
                Following the same logic, the second cookie can only go to the first child
                OR to the second child (any of the children without any cookies yet)
                '''
                if e > i:
                    continue
                new_children = children.copy()
                new_children[e] += cookies[i]
                u = min(u, solve(new_children, i+1))
                
            return u

        children = [0 for i in range(k)]
        return solve(children, 0)

        
