class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        window_start = 0
        k = 0
        max_len = 0
        last_zero_index = -1
        for window_end, num in enumerate(nums):
            if nums[window_end] == 0:
                k +=1
                
            
            if k <= 1:
                max_len = max(max_len, window_end-window_start + 1)
            if k > 1:
                window_start = last_zero_index + 1
                k -= 1
            if nums[window_end] == 0:
                last_zero_index = window_end
        return max_len
                