class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose + reverse

        def transpose(matrix):
            n = len(matrix)
            for i in range(n):
                for j in range(i + 1, n):
                    tmp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = tmp

        def reverse(matrix):
            n = len(matrix)
            for i in range(n):
                for j in range(n // 2):
                    tmp = matrix[i][j]
                    matrix[i][j] = matrix[i][n - j - 1]
                    matrix[i][n - j - 1] = tmp
         

        transpose(matrix)
        reverse(matrix)