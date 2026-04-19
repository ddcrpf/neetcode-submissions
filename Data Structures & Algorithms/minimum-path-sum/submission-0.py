class Solution:
    def minsum(self, grid, m, n, dp):
        if(m == 1 and n == 1):
            return grid[0][0]
        if(m<0 or n <0):
            return float('inf')
        if(dp[m][n]!= -1):
            return dp[m][n]
        bottom = self.minsum(grid, m -1 , n, dp)
        right = self.minsum(grid, m, n-1, dp)
        ans = grid[m-1][n-1] + min(bottom, right)
        dp[m][n] = ans
        return ans 

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1]*(n+1) for _ in range(m+1)]
        ans = self.minsum(grid, m, n, dp)
        return ans