class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n = len(grid)
        m = len(grid[0])

        maxheap = []

        for r in range(n):
            for c in range(m):
                heapq.heappush(maxheap, [-grid[r][c], r])
        
        row_count = [0] * n
        total_sum = 0
        num_elements = 0

        while maxheap and num_elements < k:
            val, row = heapq.heappop(maxheap)
            val = -val

            if row_count[row] < limits[row]:
                total_sum += val
                row_count[row] += 1
                num_elements += 1
        return total_sum