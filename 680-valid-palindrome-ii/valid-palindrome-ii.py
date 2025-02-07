class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s):
            l = 0
            r = len(s) - 1
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        
        l = 0
        r = len(s) - 1
        count = 0
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if is_palindrome(s[l + 1: r + 1]):
                    l += 1
                    count += 1
                elif is_palindrome(s[l : r]):
                    r -= 1
                    count += 1
                else:
                    return False
            if count == 2:
                return False
        
        return True