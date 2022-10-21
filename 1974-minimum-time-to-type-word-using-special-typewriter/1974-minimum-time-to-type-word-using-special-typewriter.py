class Solution:
    def minTimeToType(self, word: str) -> int:
        prev = 'a'
        ans = len(word)
        for a in word:
            dist = (ord(a) - ord(prev)) % 26
            ans += min(dist, 26 - dist)
            prev = a
        return ans
            
            