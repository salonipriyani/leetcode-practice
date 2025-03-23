class Solution:
    def climbStairs(self, n: int) -> int:
        store = [-1] * n
        def recurse(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if store[i] != -1:
                return store[i]
            store[i] = recurse(i + 1) + recurse(i + 2)
            return store[i]

        return recurse(0)