class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        n = len(nums)
        dp = set()
        dp.add(0)

        for i in range(n - 1, -1, -1):
            nextdp = set()
            for t in dp:
                nextdp.add(t)
                nextdp.add(t + nums[i])
            dp = nextdp
        
        return True if target in dp else False



        return dfs(0, sum(nums)//2)