class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for i in range(len(nums) + 1)]

        dp[0][0] = 1 # key = cursum, val = number of ways

        for i in range(len(nums)):
            for cursum, val in dp[i].items():
                dp[i + 1][cursum + nums[i]] += val
                dp[i + 1][cursum - nums[i]] += val
        
        return dp[len(nums)][target]