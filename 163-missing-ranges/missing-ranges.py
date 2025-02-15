class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        if len(nums) == 0:
            return [[lower, upper]]
        for i, num in enumerate(nums):
            if i == 0:
                if num != lower:
                    start = lower
                    end = num - 1
                    res.append([start, end])
            else:
                if nums[i] != nums[i - 1] + 1:
                    start = nums[i - 1] + 1
                    end = nums[i] - 1
                    res.append([start, end])
        if nums[len(nums) - 1] != upper:
            start = nums[len(nums) - 1] + 1
            end = upper
            res.append([start, end])
        return res