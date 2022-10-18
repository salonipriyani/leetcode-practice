class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1;
        backS = backT = 0
        while i >= 0 or j >= 0:
            
            while i >= 0:
                if s[i] == '#':
                    backS += 1
                    i-=1
                elif backS > 0:
                    backS -=1
                    i-=1
                else:
                    break
            
            while j >= 0:
                if t[j] == '#':
                    backT += 1
                    j-=1
                elif backT > 0:
                    backT -=1
                    j-=1
                else:
                    break
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            if (i >= 0) != (j >= 0):
                return False
            
            i-=1
            j-=1
        return True