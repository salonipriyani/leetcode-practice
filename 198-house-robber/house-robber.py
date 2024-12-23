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
        