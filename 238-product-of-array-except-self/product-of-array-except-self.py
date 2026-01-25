class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_prod = [1] * len(nums)

        for i in range(1, len(nums)):
            l_prod[i] = l_prod[i - 1] * nums[i - 1]
        
        r = 1
        for i in range(len(nums) - 2, -1, -1):
            l_prod[i] *= (nums[i + 1] * r)
            r*= nums[i + 1]
        return l_prod
