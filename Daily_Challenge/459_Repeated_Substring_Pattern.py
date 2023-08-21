class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        lens = len(s)
        '''
        Assume a substring length anywhere between 1 and half the string length
        '''
        for l in range(1, lens//2 + 1):
            '''
            If the string length is not divisible by the assumed substring length,
            this substring length is not a possible value. Try the next.
            '''
            if lens % l != 0:
                continue
            '''
            Now iterate the string.
            '''
            i = 0
            while True:
                if s[i*l:(i+1)*l] != s[:l]:
                    break
                if (i+1)*l == lens:
                    '''
                    If all checks were good and we are exactly at the end of the string
                    return True
                    '''
                    return True
                i += 1
        return False
