class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        start = -1
        while i < len(haystack):

            if needle[0] == haystack[i]:
                haystack_st = i
                j = 0
                while i < len(haystack) and j < len(needle) and haystack[i] == needle[j]:
                    i += 1
                    j += 1
                if j == len(needle):
                    start = i - len(needle)
                    return start
                else:
                    i = haystack_st + 1
            else:
                i += 1
        return start