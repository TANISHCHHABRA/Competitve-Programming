class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        b = [0]*n
        b[0] = 1
        b[1] = 2
        for i in range(2,n):
            b[i] = b[i-1] + b[i-2]
        return b[-1]  
