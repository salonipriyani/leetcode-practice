class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque()
        q.append(0)
        seen = set()
        dict_set = set(wordDict)
        while q:
            i = q.popleft()
            if i == len(s):
                return True
            for j in range(i + 1, len(s) + 1):
                if j in seen:
                    continue
                if s[i : j] in dict_set:
                    q.append(j)
                    seen.add(j)
        
        return False