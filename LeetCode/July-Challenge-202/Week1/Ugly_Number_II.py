class Solution:
    def nthUglyNumber(self, n: int) -> int:
        l = [1]
        for i in range(n):
            if l[i]*2 not in l:
                l.append(l[i]*2)
            if l[i]*3 not in l:
                l.append(l[i]*3)
            if l[i]*5 not in l:
                l.append(l[i]*5)
            l.sort()

        return l[n-1]
