class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        left = 0
        right = len(nums) - 1
        max_sum = 0
        while left < right:
            sum_nums = nums[left] + nums[right]
            if sum_nums < k:
                max_sum = max(max_sum, sum_nums)
                left +=1
            else:
                right -=1 
        
        if max_sum == 0:
            return -1
        return max_sum