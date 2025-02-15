class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        def dfs(r, c):
            if (r, c) in visited:
                return
            
            if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] == "1":
                visited.add((r,c))
                dfs(r + 1, c)
                dfs(r, c + 1)
                dfs(r - 1, c)
                dfs(r, c - 1)


        

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r, c)
                    res += 1
        return res