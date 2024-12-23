#Recursion: Time = O(2 ^ n), space = O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dfs(i):
            if i >= len(nums):
                return 0
            return max(nums[i] + dfs(i + 2), dfs(i + 1))
        
        return dfs(0)

#Recursion - top-down: Time = O(n), space = O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return memo[i]
        dfs(0)
        return memo[0]
#Recursion - bottom-up: Time = O(n), space = O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp = [0] * (len(nums))

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        
        return dp[n - 1]