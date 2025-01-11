class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        m = len(word1)
        n = len(word2)
        def dfs(i, j):
            if i == len(word1):
                return n - j
            if j == len(word2):
                return m - i

            if (i, j) in dp:
                return dp[(i, j)]

            if word1[i] == word2[j]:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                res = min(dfs(i + 1, j), dfs(i, j + 1), dfs(i + 1, j + 1))
                dp[(i, j)] = res + 1
            return dp[(i, j)]
        return dfs(0, 0)
