class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        lower_bound = self.findbound(nums, True, target)
        if lower_bound == -1:
            return [-1, -1]
        upper_bound = self.findbound(nums, False, target)
        return [lower_bound, upper_bound]
    
    def findbound(self, nums, islower, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                if islower:
                    if l == mid or nums[mid - 1] != nums[mid]:
                        return mid
                    else:
                        r = mid - 1
                else:
                    if r == mid or nums[mid + 1] != nums[mid]:
                        return mid
                    else:
                        l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1