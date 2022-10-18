class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq_map = {}
        
        for i in s:
            if i not in freq_map:
                freq_map[i] = 0
            freq_map[i] += 1
        
        for i in range(len(s)):
            if freq_map[s[i]] == 1:
                return i
        
        return -1