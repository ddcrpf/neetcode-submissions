class Solution:
    def paths(self, m, n,dp):
        if(m == 1 and n ==1 ):
            return 1
        if(m<0 or n < 0):
            return 0
        if(dp[m][n] != 0):
            return dp[m][n]

        bottom = self.paths(m-1, n, dp)
        right = self.paths(m, n-1, dp)
        dp[m][n] = bottom + right
        return bottom + right
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        return self.paths(m,n, dp)

        