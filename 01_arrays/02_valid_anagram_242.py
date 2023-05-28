```
Instead of implementing a hashmap, as done is the previous solution,
let us make use of the Counter from the python collections package.

The follow up "What if the inputs contain Unicode characters?" is not an issue
of python3 where all strings are unicode strings.

Room for improvement: Since we are dealing with only 26 characters 
(as opposed a near infinite number of integers in the previous challenge)
the hash counter can actually be of space complexity O(1) because it only 
ever needs to map 26 keys. This is given to the reader as an exercise... ;)
```

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = Counter(s)
        freq2 = Counter(t)
        return freq1 == freq2
