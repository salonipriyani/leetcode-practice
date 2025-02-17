class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = 1
        b = min(m - 1, n - 1)
        a = m + n - 2
        for i in range(b):
            res = res * (a - i) // (i + 1)

        return res