class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq_map = {}

        for char in t:
            if char not in t_freq_map:
                t_freq_map[char] = 0
            t_freq_map[char] += 1
        formed = 0
        required = len(t_freq_map)
        l = 0
        min_window = float('inf')
        min_l = 0
        min_r = 0
        window_freq = {}
        for r in range(len(s)):
            
            if s[r] not in window_freq:
                window_freq[s[r]] = 0
            window_freq[s[r]] += 1
            if s[r] in t_freq_map and t_freq_map[s[r]] == window_freq[s[r]]:
                formed += 1
            while l <= r and required == formed:
                window_size = r - l + 1
                if window_size < min_window:
                    min_window = window_size
                    min_l = l
                    min_r = r

                window_freq[s[l]] -= 1
                if s[l] in t_freq_map and window_freq[s[l]] < t_freq_map[s[l]]:
                    formed -= 1
                l += 1
            
        return "" if min_window == float('inf') else s[min_l : min_r + 1]
