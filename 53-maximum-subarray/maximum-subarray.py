class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sub_sum = max_sub_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sub_sum = max(nums[i], curr_sub_sum + nums[i])
            max_sub_sum = max(curr_sub_sum, max_sub_sum)
        return max_sub_sum
