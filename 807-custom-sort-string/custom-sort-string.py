class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq_map = {}
        for char in s:
            if char not in freq_map:
                freq_map[char] = 0
            freq_map[char] += 1
        res = ""
        for char in order:
            if char in freq_map:
                freq = freq_map[char]
                while freq != 0:
                    res += char
                    freq -= 1
                freq_map[char] = 0
        for char, freq in freq_map.items():
            if freq != 0:
                while freq != 0:
                    res += char
                    freq -= 1

        return res