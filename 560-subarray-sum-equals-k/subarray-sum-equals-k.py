class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_map = {0: 1}
        count = 0
        sum = 0
        for num in nums:
            sum += num
            if (sum - k) in sum_map:
                count += sum_map[sum - k]
            if sum not in sum_map:
                sum_map[sum] = 0
            sum_map[sum] += 1
        
        return count