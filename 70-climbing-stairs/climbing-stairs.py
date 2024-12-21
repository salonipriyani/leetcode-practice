class Solution:
    def climbStairs(self, n: int) -> int:
        #Recursion
        #Time complexity: 2 ^ n, Space = O(n)
        def dfs(i):
            if i > n:
                return 0
            elif i == n:
                return 1

            return dfs(i + 1) + dfs(i + 2)
        
        return dfs(0)

#Top down - recursion but with cache
class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n
        
        def dfs(i):
            if i > n:
                return 0
            elif i == n:
                return 1
            if cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        
        return dfs(0)
        
