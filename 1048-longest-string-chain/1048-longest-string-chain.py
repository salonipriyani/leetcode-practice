class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words_present = set(words)
        memo = {}
        ans = 0
        for word in words:
            ans = max(ans, self.dfs(word, memo, words_present))
            
        return ans
            
    def dfs(self, currWord, memo, words_present):
        if currWord in memo:
            return memo[currWord]
        
        maxLength = 1
        
        for i in range(len(currWord)):
            newWord = currWord[:i] + currWord[i+1:]
            
            if newWord in words_present:
                currLength = 1 + self.dfs(newWord, memo, words_present)
                maxLength = max(maxLength, currLength)
            
        memo[currWord] = maxLength
        return maxLength
    
    
                