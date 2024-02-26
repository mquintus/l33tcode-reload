# 2709 - Greatest Common Divisor Traversal
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        for el in nums:
            if el == 1:
                return False

        nums = list(set(nums))
        n = len(nums)
        if n == 1:
            return True
        numsset = set(nums)

        global count_connected
        count_connected = 1
        is_connected = {}
        for el in nums:
            is_connected[el] = set()

        maxnum = max(nums)
        minnum = min(nums)

        def SieveOfEratosthenes(maxnum):
            prime_list = [True] * (maxnum + 10)
            prime_list[0] = False
            prime_list[1] = False

            prime_arr = []
            for i in range(maxnum + 10):
                if prime_list[i] == True:
                    prime_arr.append(i)
                    for j in range(i, maxnum+10, i):
                        prime_list[j] = False
                        if j in numsset:
                            is_connected[j].add(i)
                            if i not in is_connected: 
                                is_connected[i] = set()
                            is_connected[i].add(j)

            return prime_arr
        prime_list = SieveOfEratosthenes(maxnum)
        #print('len(prime_list)', len(prime_list))
        #for key, val in is_connected.items():
            #print('key, val: ', end = '')
            #print(key, val)

        for prime, connections in is_connected.items():
            if len(connections) == 1 and prime in connections:
                #print("Only self-referential")
                return False

        #biggest_prime = max(is_connected.keys())
        #for p in is_connected.keys():
        #    if p != biggest_prime and p > biggest_prime / 2:
        #        return False

        m = len(is_connected.keys())
        visited_primes = set()
        states = [list(is_connected.keys())[0]]
        while states and count_connected < m:
            #print("states",states)
            prime = states.pop()
            visited_primes.add(prime)
            #print('is_connected[prime]', prime, is_connected)
            for next_prime in is_connected[prime]:
                #print("next_prime", next_prime)
                if next_prime not in visited_primes:
                    states.append(next_prime)
                    visited_primes.add(next_prime)
                    count_connected += 1
                    if count_connected == m:
                            break
                if count_connected == m:
                    break
            
        #print("count_connected",count_connected)
        return count_connected == m

            

