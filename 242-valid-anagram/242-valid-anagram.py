class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;
        
        freq = []
        for i in range(26):
            freq.append(0)
            
        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] = freq[ord(s[i]) - ord('a')] + 1
            freq[ord(t[i]) - ord('a')] = freq[ord(t[i]) - ord('a')] - 1
            
        for count in freq:
            if count != 0:
                return False
        
        return True