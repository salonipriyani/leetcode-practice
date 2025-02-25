class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        set1 = set()
        set2 = set()

        for r in range(len(mat1)):
            for c in range(len(mat1[0])):
                if mat1[r][c] != 0:
                    set1.add((r, c))
        
        for r in range(len(mat2)):
            for c in range(len(mat2[0])):
                if mat2[r][c] != 0:
                    set2.add((r, c))
        
        res = [[0] * len(mat2[0]) for i in range(len(mat1))]
        for r in range(len(mat1)):
            row = mat1[r]
            for i in range(len(row)):
                row_element = row[i]
                if row_element:
                    for c in range(len(mat2[i])):
                        res[r][c] += row_element * mat2[i][c]
        return res