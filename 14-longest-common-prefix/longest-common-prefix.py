class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""

        
        s = strs[0]
        for i in range(len(s)):
            flag = 0
            for j in range(1, len(strs)):
                s2 = strs[j]
                if i >= len(s2) or (i < len(s2) and s[i] != s2[i]):
                    flag = 1
            if flag == 0:
                pre += s[i]
            if flag == 1:
                break
        return pre