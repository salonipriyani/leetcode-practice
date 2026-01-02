class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, currList, total):
            if i >= len(candidates) or total > target:
                return

            if total == target:
                res.append(currList.copy())
                return

            currList.append(candidates[i])
            dfs(i, currList.copy(), total + candidates[i])
            currList.pop()
            dfs(i + 1, currList.copy(), total)
        
        dfs(0, [], 0)
        return res