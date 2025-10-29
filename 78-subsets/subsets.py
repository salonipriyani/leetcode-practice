class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, curr_list):
            if i == len(nums):
                res.append(curr_list)
                return
            backtrack(i + 1, curr_list.copy())
            curr_list.append(nums[i])
            backtrack(i + 1, curr_list.copy())


        backtrack(0, [])
        return res