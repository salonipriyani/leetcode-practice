class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_start = max_len = max_repeat_char = 0
        char_freq_map = {}
        for window_end in range(len(s)):
            right_char = s[window_end]
            
            if right_char not in char_freq_map:
                char_freq_map[right_char] = 0
            char_freq_map[right_char] += 1
            
            max_repeat_char = max(max_repeat_char, char_freq_map[right_char])
            
            window_size = window_end - window_start + 1
            if (window_size - max_repeat_char) > k:
                left_char = s[window_start]
                char_freq_map[left_char] -= 1
                window_start += 1
                
            max_len = max(max_len, window_end - window_start + 1)
        
        return max_len