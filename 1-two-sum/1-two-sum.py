class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        res = []
        for i in range(len(nums)):
            map[target - nums[i]] = i
            
        for i in range(len(nums)):
            if nums[i] in map:
                if map[nums[i]] != i:
                    res.append(map[nums[i]])
                    res.append(i)
                    break
                    
        return res