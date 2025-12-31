
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums: List[int]) -> int:
        ls = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if ls[i] != -1:
                return ls[i]
            ls[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return ls[i]
        
        return dfs(0)