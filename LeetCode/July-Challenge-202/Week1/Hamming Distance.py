class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        X = bin(x)[2:]
        Y = bin(y)[2:]
        if len(X) < len(Y):
            X = '0'*(len(Y) - len(X)) + X
        elif len(X) > len(Y):
            Y = '0'*(len(X) - len(Y)) + Y
        
        ans = 0
        x = list(X)
        y = list(Y)
        x.reverse()
        y.reverse()
        for i in range(len(x)):
            if x[i] != y[i]:
                ans += 1
        return ans
