class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        groups = {}
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                val = matrix[r][c]
                if (r - c) not in groups:
                    groups[r-c] = val
                if groups[r-c] != val:
                    return False
        return True