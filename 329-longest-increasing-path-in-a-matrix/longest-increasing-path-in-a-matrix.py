class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        leaves = []
        outdegrees = {}
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                outdegrees[(r, c)] = 0
                for dir in dirs:
                    new_r = r + dir[0]
                    new_c = c + dir[1]
                    if new_r >= 0 and new_r < len(matrix) and new_c >= 0 and new_c < len(matrix[0]) and matrix[new_r][new_c] > matrix[r][c]:
                        outdegrees[(r, c)] += 1
        

        leaves = []
        for cell in outdegrees:
            if outdegrees[cell] == 0:
                leaves.append(cell)

        height = 0
        while leaves:
            height += 1
            newleaves = []
            for i in range(len(leaves)):
                r, c = leaves[i]
                for dr, dc in dirs:
                    new_r = r + dr
                    new_c = c + dc
                    if new_r >= 0 and new_r < len(matrix) and new_c >= 0 and new_c < len(matrix[0]) and matrix[new_r][new_c] < matrix[r][c]:
                        outdegrees[(new_r, new_c)] -= 1
                        if outdegrees[(new_r, new_c)] == 0:
                            newleaves.append([r + dr, c + dc])
            
            leaves = newleaves
        
        return height
