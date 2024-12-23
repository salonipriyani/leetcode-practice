#Recursion - Time = O(2^n), Space = O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        def dfs(i):
            if i >= n:
                return 0
            return cost[i] + min(dfs(i+1), dfs(i+2))


        return min(dfs(0), dfs(1))

# Top down - Time = O(n), space = O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0
            if total[i] != -1:
                return total[i]
            total[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return total[i]

        return min(dfs(0), dfs(1))

# Bottom up - Time = O(n), space = O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i -  1], dp[i - 2] + cost[i - 2])

        return dp[n]