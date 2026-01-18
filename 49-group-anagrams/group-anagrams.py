class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        letter_map = {}
        for i in range(len(strs)):
            string = strs[i]
            freq = [0] * 26
            for char in string:
                freq[ord(char) - ord('a')] += 1
            if tuple(freq) not in letter_map:
                letter_map[tuple(freq)] = []
            letter_map[tuple(freq)].append(string)
        
        return [value for value in letter_map.values()]
