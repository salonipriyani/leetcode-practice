class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        q = deque() # store [r, c, dist]
        q.append([0, 0, 1])
        n = len(grid) - 1
        def get_neighbors(r, c):
            nei = []
            for i, j in [[1, 0], [0, 1], [1, 1], [0, -1], [-1, 0], [-1, -1], [-1, 1], [1, -1]]:
                if not (0 <= r + i <= n and 0 <= c + j <= n):
                    continue
                if grid[r + i][c + j] != 0:
                    continue
                nei.append([r + i, c + j])
            return nei
        if grid[0][0] != 0 or grid[n][n] != 0:
            return -1
        visited = set()
        visited.add((0, 0))
        while q:
            r, c, dist = q.popleft()
            if r == n and c == n:
                return dist
            for nei_r, nei_c in get_neighbors(r, c):
                if (nei_r, nei_c) in visited:
                    continue
                visited.add((nei_r, nei_c))
                q.append([nei_r, nei_c, dist + 1])
        return -1