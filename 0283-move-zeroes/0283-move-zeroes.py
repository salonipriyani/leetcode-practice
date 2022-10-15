class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        index_after_last_non_zero = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index_after_last_non_zero] = nums[i]
                index_after_last_non_zero = index_after_last_non_zero + 1
        
        for i in range(index_after_last_non_zero, len(nums)):
            nums[i] = 0
        
            