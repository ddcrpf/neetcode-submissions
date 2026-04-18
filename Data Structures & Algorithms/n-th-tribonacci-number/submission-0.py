class Solution:
    def trib(self, n, dp ):
        if(n<= 1 and n>=0):
             return n
        if(n<0):
            return 0
        if(dp[n]!= 0):
             return dp[n]
        ans = self.trib(n-1, dp) + self.trib(n-2, dp) + self.trib(n-3, dp)
        dp[n] = ans
        return ans

    def tribonacci(self, n: int) -> int:
        dp = [0]*(n+1)
        ans = self.trib(n, dp)
        return ans

