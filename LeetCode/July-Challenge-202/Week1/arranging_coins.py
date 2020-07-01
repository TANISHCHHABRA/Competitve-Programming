class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = 0
        x = n
        for i in range(1,n+1):
            if x >= i:
                x = x - i
                ans += 1
            else:
                break
        return ans
