class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        char_set = set()
        max_window_size = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            window_size = r - l + 1
            print(s[l : r + 1])
            if window_size > max_window_size:
                max_window_size = window_size
        
        return max_window_size