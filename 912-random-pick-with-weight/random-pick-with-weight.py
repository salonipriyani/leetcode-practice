class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.prefix_sum = [w[0]]
        for i in range(1, len(w)):
            self.prefix_sum.append(self.prefix_sum[i - 1] + w[i])
        self.total_sum = sum(w)

    def pickIndex(self) -> int:
        random_int = random.randint(1, self.total_sum)
        l = 0
        r = len(self.prefix_sum) - 1
        while l < r:
            mid = (l + r) // 2
            if random_int > self.prefix_sum[mid]:
                l = mid + 1
            else:
                r = mid
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()