class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_dict_set = set(wordDict)

        res = []
        def dfs(i, curr_sen):
            if i == len(s):
                res.append(' '.join(curr_sen))
                return

            for j in range(i + 1, len(s) + 1):
                word = s[i : j]
                if word in word_dict_set:
                    curr_sen.append(word)
                    dfs(j, curr_sen)
                    curr_sen.pop()

        dfs(0, [])
        return res