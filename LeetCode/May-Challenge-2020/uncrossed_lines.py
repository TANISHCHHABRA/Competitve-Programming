class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        len_a = len(A)
        len_b = len(B)

        if len_a==0 or len_b==0: return 0;
        dp = [[0 for i in range(len_b+1)] for j in range(len_a+1)]

        for i in range(len_a):
            for j in range(len_b):
                dp[i+1][j+1]=dp[i][j]+1 if A[i]==B[j] else max(dp[i+1][j], dp[i][j+1])

        return dp[len_a][len_b]
