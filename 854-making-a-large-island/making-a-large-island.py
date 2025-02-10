class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        def explore_island(island_id, r, c):
            if not (r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] == 1):
                return 0
            
            grid[r][c] = island_id

            return (1 +
                    explore_island(island_id, r + 1, c) + explore_island(island_id, r, c + 1) + 
                    explore_island(island_id, r - 1, c) + explore_island(island_id, r, c - 1))

        island_sizes = {}
        island_id = 2
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    island_sizes[island_id] = explore_island(island_id, r, c)
                    island_id += 1
        
        if len(island_sizes) == 0:
            return 1
        
        if len(island_sizes) == 1:
            island_id = 2
            if island_sizes[island_id] == len(grid) * len(grid[0]):
                return island_sizes[island_id]
            return island_sizes[island_id] + 1
        max_island_size = 1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    nei_islands = set()
                    if r + 1 < len(grid) and grid[r + 1][c] > 1:
                        nei_islands.add(grid[r + 1][c])
                    if r - 1 >= 0 and grid[r - 1][c] > 1:
                        nei_islands.add(grid[r - 1][c])
                    if c + 1 < len(grid[0]) and grid[r][c + 1] > 1:
                        nei_islands.add(grid[r][c + 1])
                    if c - 1 >= 0 and grid[r][c - 1] > 1:
                        nei_islands.add(grid[r][c - 1])
                    island_size = 1
                    for island_id in nei_islands:
                        island_size += island_sizes[island_id]
                    if island_size > max_island_size:
                        max_island_size = island_size
        return max_island_size
        
        