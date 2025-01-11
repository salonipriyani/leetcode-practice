class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                    #visited.add((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        t = 0
        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                for a, b in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                    if a >= 0 and b >= 0 and a < rows and b < cols and grid[a][b] == 1:
                        #visited.add((a, b))
                        q.append([a, b])
                        grid[a][b] = 2
                        fresh -= 1
            t += 1
        if fresh == 0:
            return t
        return -1