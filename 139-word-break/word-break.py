class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque()
        seen = set()
        wordset = set(wordDict)
        
        q.append(0)
        while q:
            i = q.popleft()
            if i == len(s):
                return True
            for j in range(i + 1, len(s) + 1):
                if j in seen:
                    continue
                elif s[i : j] in wordset:
                    q.append(j)
                    seen.add(j)
        return False