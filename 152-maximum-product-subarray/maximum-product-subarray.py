class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = 1
        res = float(-inf)
        for num in nums:
            tmp = curMax * num
            curMax = max(curMin * num, curMax * num, num)
            curMin = min(tmp, curMin * num, num)
            res = max(res, curMax)

        return res
        
        
