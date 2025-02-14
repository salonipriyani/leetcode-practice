class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.ind_map = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in self.ind_map:
                self.ind_map[num] = []
            self.ind_map[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.ind_map[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)