class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        leaves = []
        dirs = [[0,1], [1, 0], [-1, 0], [0, -1]]
        outdegrees = {}
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                outdegrees[(r,c)] = 0
                for dr, dc in dirs:
                    if r + dr >= 0 and r + dr < len(matrix) and c + dc >= 0 and c + dc < len(matrix[0]) and matrix[r + dr][c + dc] > matrix[r][c]:
                        outdegrees[(r,c)] += 1
        
        for rc, out in outdegrees.items():
            r, c = rc
            if outdegrees[rc] == 0:
                leaves.append([r, c])
        height = 0
        while leaves:
            height += 1
            newLeaves = []
            for i in range(len(leaves)):
                r, c = leaves[i]
                for dr, dc in dirs:
                    if r + dr >= 0 and r + dr < len(matrix) and c + dc >= 0 and c + dc < len(matrix[0]) and matrix[r + dr][c + dc] < matrix[r][c]:
                        outdegrees[(r + dr, c + dc)] -= 1
                        if outdegrees[(r + dr, c + dc)] == 0:
                            newLeaves.append([r + dr, c + dc])
            
            leaves = newLeaves
        return height
         
