class Solution:
    def climbStairs(self, n: int) -> int:
        store = [0] * (n + 1)
        if n < 3: return n
        store[1] = 1
        store[2] = 2
        for i in range(3, n + 1):
            store[i] = store[i - 1] + store[i - 2]
        
        return store[n]