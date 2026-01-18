class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = [[0] * 26 for s in strs]
        letter_map = {}
        for i in range(len(strs)):
            string = strs[i]
            for char in string:
                freq[i][ord(char) - ord('a')] += 1
            if tuple(freq[i]) not in letter_map:
                letter_map[tuple(freq[i])] = []
            letter_map[tuple(freq[i])].append(string)
        
        return [value for value in letter_map.values()]
