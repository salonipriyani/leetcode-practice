class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq_map = {}
        

        for char in t:
            if char not in t_freq_map:
                t_freq_map[char] = 0
            t_freq_map[char] += 1
        
        required = len(t_freq_map)
        formed = 0
        min_window = float('inf')
        min_l = 0
        min_r = 0
        l = 0
        window_counts = {}
        for r, char in enumerate(s):
            print(char)
            print(s[l])
            if char not in window_counts:
                window_counts[char] = 0
            window_counts[char] += 1
            
            if char in t_freq_map and t_freq_map[char] == window_counts[char]:
                formed += 1
            
            while l <= r and formed == required:

                window_size = r - l + 1
                if window_size < min_window:
                    min_window = window_size
                    min_l = l
                    min_r = r

                window_counts[s[l]] -= 1
                if s[l] in t_freq_map and window_counts[s[l]] < t_freq_map[s[l]]:
                    formed -= 1
                l += 1
            

            
            
        return "" if min_window == float('inf') else s[min_l : min_r + 1]
