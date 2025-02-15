class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand(l ,r):
            while l >=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        res_l, res_r = 0, 0
        for i in range(len(s)):
            odd_length = expand(i, i)
            if odd_length > res_r - res_l + 1:
                dist = odd_length // 2
                res_l = i - dist
                res_r = i + dist

            even_length = expand(i, i + 1) 
            if even_length > res_r - res_l + 1:
                dist = (even_length // 2) - 1
                res_l = i - dist
                res_r = i + dist + 1
        
        return s[res_l : res_r + 1]