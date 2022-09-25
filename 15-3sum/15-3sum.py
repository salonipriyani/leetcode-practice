class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.addToList(res, -nums[i], i + 1, nums)
        return res
            
    def addToList(self, res: List[int], targetSum: int, left: int, nums: List[int]):
        right = len(nums) - 1

        while (left < right):
            if nums[left] + nums[right] == targetSum:
                res.append([-targetSum, nums[left], nums[right]])
                left+=1
                right-=1
                while left < right and nums[left] == nums[left - 1]:
                    left+=1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] < targetSum:
                left += 1
            else:
                right -= 1
            