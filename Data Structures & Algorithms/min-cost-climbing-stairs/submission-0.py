class Solution:

    def func(self, n, cost, dp):
        if(n<=1):
            return cost[n]
        if(dp[n]!=-1):
            return dp[n]
        ans = cost[n] + min(self.func(n-1, cost, dp), self.func(n-2, cost, dp))
        dp[n] = ans
        return ans



    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1]*len(cost)
        n = len(cost) - 1
        ans = min(self.func(n, cost, dp),self.func(n-1, cost, dp))
        return ans
        