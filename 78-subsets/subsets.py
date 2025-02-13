class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, curr_ls):
            
            if i == len(nums): 
                res.append(curr_ls.copy())               
                return
            dfs(i + 1, curr_ls.copy())
            curr_ls.append(nums[i])
            dfs(i + 1, curr_ls.copy())

        dfs(0, [])
        return res        