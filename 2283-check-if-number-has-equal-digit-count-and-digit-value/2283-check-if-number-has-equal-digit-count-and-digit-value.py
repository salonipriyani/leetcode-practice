class Solution:
    def digitCount(self, num: str) -> bool:
        freq_map = {}
        
        for i in range(len(num)):
            freq_map[i] = 0
        
        for i in range(len(num)):
            if int(num[i]) in freq_map:
                freq_map[int(num[i])] += 1
        
        print(freq_map)
        for i in range(len(num)):
            if int(num[i]) != freq_map[i]:
                return False
        
        return True