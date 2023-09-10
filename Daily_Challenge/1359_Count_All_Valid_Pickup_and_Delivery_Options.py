class Solution:
    def countOrders(self, n: int) -> int:
        mod = 1e9 + 7
        
        ans = 1
        for i in range(2, n + 1):
            ans = (ans * (2 * i - 1) * i) % mod
        return int(ans % mod)
