class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        invalues = [0] * (N+1)
        outvalues = [0] * (N+1)
        
        for a,b in trust:
            outvalues[a]+=1
            invalues[b]+=1
        
        for i in range(1,N+1):
            if outvalues[i]==0 and invalues[i]==N-1:
                return i
        return -1
