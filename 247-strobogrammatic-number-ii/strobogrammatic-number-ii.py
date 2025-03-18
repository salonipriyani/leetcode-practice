class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        res = []
        def backtracking(l, r, curr):
            if l > r:
                res.append(''.join(curr))
                return
            
            for a, b in pairs:
                if l == r and a != b:
                    continue
                if l == 0 and a == '0' and n > 1:
                    continue
                curr[l] = a
                curr[r] = b
                backtracking(l + 1, r - 1, curr)

        
        pairs = [['1' , '1'], ['0', '0'], ['8', '8'], ['6', '9'], ['9', '6']]
        backtracking(0, n - 1, [''] * n)
        return res