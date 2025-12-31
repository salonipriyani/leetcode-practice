class Solution:
    def rob(self, nums: List[int]) -> int:
        ls = [0] * len(nums)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        ls[0], ls[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            ls[i] = max(nums[i] + ls[i - 2], ls[i - 1])

        return ls[len(nums) - 1]

