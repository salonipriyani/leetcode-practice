class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(l, r):
            num_palindromes = 0
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
                num_palindromes += 1
            return num_palindromes
        

        res = 0
        for i in range(len(s)):
            # odd
            res += expand(i, i)

            #even 
            res += expand(i, i + 1)
        return res