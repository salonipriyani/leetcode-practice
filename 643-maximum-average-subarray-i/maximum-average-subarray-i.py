class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = i + k
        max_avg = 0.0
        sum = 0
        for i in range(k):
            sum += nums[i]
        max_sum = sum
        for i in range(k, len(nums)):
            sum = sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, sum)
        
        return max_sum / k