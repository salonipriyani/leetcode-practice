# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> None:
#        
#
#    def isTarget(self) -> bool:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        reverse_dir = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
        
        grid = {}  # Store the explored grid
        target = None
        
        # Step 1: DFS to map the grid (avoid too many master API calls)
        def dfs(r, c):
            nonlocal target
            if (r, c) in grid:  # Already visited
                return
            
            if master.isTarget():
                target = (r, c)

            grid[(r, c)] = 1  # Mark as accessible
            
            for d, (dr, dc) in directions.items():
                nr, nc = r + dr, c + dc
                if (nr, nc) not in grid and master.canMove(d):
                    master.move(d)
                    dfs(nr, nc)
                    master.move(reverse_dir[d])  # Move back
        
        dfs(0, 0)
        
        if target is None:  
            return -1  # If no target found, return -1
        
        # Step 2: BFS to find the shortest path
        queue = deque([(0, 0, 0)])  # (row, col, distance)
        visited = set([(0, 0)])

        while queue:
            r, c, dist = queue.popleft()
            if (r, c) == target:
                return dist

            for dr, dc in directions.values():
                nr, nc = r + dr, c + dc
                if (nr, nc) in grid and (nr, nc) not in visited:
                    queue.append((nr, nc, dist + 1))
                    visited.add((nr, nc))

        return -1  # If target is unreachable



