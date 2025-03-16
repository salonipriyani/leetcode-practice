class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        

        total = sum(nums)
        numset = set(nums)
        num_map = {}

        for num in nums:
            if num not in num_map:
                num_map[num] = 0
            num_map[num] += 1

        largest = float('-inf')
        for num in nums:
            potential_outlier = total - 2 * num

            if potential_outlier in num_map and (potential_outlier != num or num_map[num] > 1):
                largest = max(largest, potential_outlier)

        return largest