class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # binary search
        # edge case - at index 0, number at index -1 <
        # num at index n < num at index n-1
        # if num at mid is not greater than its neighbors, move window to side with greater number

        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2
        while l < r:
            mid = (l + r) // 2
            if (mid == 0 and nums[mid] > nums[mid + 1]) or (mid == len(nums) - 1 and nums[mid] > nums[mid - 1]) or (nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]):
                return mid
            elif (mid != 0 and nums[mid - 1] > nums[mid]):
                r = mid
            elif mid != len(nums) - 1 and nums[mid + 1] > nums[mid]:
                l = mid + 1
        return l