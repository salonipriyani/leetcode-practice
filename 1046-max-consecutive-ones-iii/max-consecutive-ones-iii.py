class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        max_one_count = 0
        curr_zero_count = 0
        for r in range(len(nums)):
            
            if nums[r] == 0:
                curr_zero_count += 1
                #if curr_zero_count > k:
                while curr_zero_count > k:
                    if nums[l] == 0:
                        curr_zero_count -= 1
                    l += 1
            window_size = r - l + 1
            max_one_count = max(max_one_count, window_size)
        return max_one_count  
            