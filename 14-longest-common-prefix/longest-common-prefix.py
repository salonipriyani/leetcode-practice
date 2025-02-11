class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        
        s = strs[0]
        for i in range(len(s)):
            for j in range(1, len(strs)):
                s2 = strs[j]
                if i >= len(s2) or (i < len(s2) and s[i] != s2[i]):
                    return pre

            pre += s[i]
        return pre

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        strs.sort()  # Sort lexicographically
        first, last = strs[0], strs[-1]
        i = 0

        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1  # Count matching characters

        return first[:i]  # Return the common prefix