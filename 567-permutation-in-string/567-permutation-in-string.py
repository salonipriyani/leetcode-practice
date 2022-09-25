class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_freq_map = {}
        
        for char in s1:
            if char not in char_freq_map:
                char_freq_map[char] = 0
            char_freq_map[char] += 1
        window_start = 0
        matched = 0
        for window_end in range(len(s2)):
            right_char = s2[window_end]
            
            if right_char in char_freq_map:
                char_freq_map[right_char] -= 1
                if char_freq_map[right_char] == 0:
                    matched += 1
            
            if matched == len(char_freq_map):
                return True
            
            if (window_end - window_start  + 1 >= len(s1)):
                left_char = s2[window_start]
                if left_char in char_freq_map:
                    if char_freq_map[left_char] == 0:
                        matched -= 1
                    char_freq_map[left_char] += 1
                window_start += 1
            
            
        return False