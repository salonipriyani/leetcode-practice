class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_int = 0
        while x > reversed_int:
            reversed_int = reversed_int * 10 + (x % 10)
            x = x // 10
        
        return reversed_int == x or reversed_int // 10 == x