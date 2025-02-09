class Solution:
    def isNumber(self, s: str) -> bool:
        seenDigit = seenDot = seenExponent = False

        for i, char in enumerate(s):
            if char.isdigit():
                seenDigit = True
            
            elif char in ('+', '-'):
                if i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
            
            elif char in ('e', 'E'):
                if not seenDigit or seenExponent:
                    return False
                seenDigit = False
                seenExponent = True

            elif char == '.':
                if seenDot or seenExponent:
                    return False
                seenDot = True
            else:
                return False
        return seenDigit