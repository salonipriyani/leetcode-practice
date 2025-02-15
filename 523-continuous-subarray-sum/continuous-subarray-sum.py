class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        premod = 0
        modSeen = {0 : -1}
        for i in range(len(nums)):
            premod = (premod + nums[i]) % k
            
            if premod in modSeen:
                if i - modSeen[premod] > 1:
                    return True
            else:
                modSeen[premod] = i
        return False