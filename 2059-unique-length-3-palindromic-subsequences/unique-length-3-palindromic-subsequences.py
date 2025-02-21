class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26
        for i, char in enumerate(s):
            curr = ord(char) - ord('a')
            if first[curr] == -1:
                first[curr] = i
            last[curr] = i
        res = 0
        for i in range(26):
            if first[i] != -1:
                between = set()
                for j in range(first[i] + 1, last[i]):
                    between.add(s[j])
                res += len(between)
        
        return res