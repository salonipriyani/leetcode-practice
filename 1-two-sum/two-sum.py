class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = {}

        for i in range(len(nums)):
            num = nums[i]
            second_num = target - num
            if second_num in sum_map and i != sum_map[second_num]:
                return[i, sum_map[second_num]]
            sum_map[num] = i
        