class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = window_start = 0
        char_index_map = {}
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char in char_index_map:
                window_start = max(window_start, char_index_map[right_char] + 1)
            char_index_map[right_char] = window_end
            max_len = max(max_len, window_end - window_start + 1)
        return max_len
            
                