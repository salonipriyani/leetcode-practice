class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        up_dir = True
        i = j = 0
        res = []
        while True:
            res.append(mat[i][j])
            if i == len(mat) - 1 and j == len(mat[0]) - 1:
                return res
            
            if up_dir:
                if j == len(mat[0]) - 1:
                    i += 1
                    up_dir = False
                elif i - 1 < 0:
                    j += 1
                    up_dir = False
                else:
                    i -= 1
                    j += 1
            else:
                if i + 1 > len(mat) - 1:
                    j += 1
                    up_dir = True
                elif j - 1 < 0:
                    i += 1
                    up_dir = True
                
                else:
                    i += 1
                    j -= 1
        return res