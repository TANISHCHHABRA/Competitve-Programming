from collections import deque
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        l = []
        if n==1:
            for i in range(0,10):
                l.append(i)
            return l
        l = deque(l)
        for i in range (1,10):
            if i+k<=9 or i-k>=0:
                l.append(i)
        for i in range (2,n+1):
            s = len(l)
            while s:
                t = l.popleft()
                s -= 1
                d = t%10
                if d+k<=9:
                    l.append((10*t)+d+k)
                if d-k>=0 and k!=0:
                    l.append((10*t)+d-k)
        return l
