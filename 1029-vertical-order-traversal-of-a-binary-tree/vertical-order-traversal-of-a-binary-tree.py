# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_map = {} # (row, col) : [] of nodes
        min_idx = 0
        max_idx = 0
        if not root:
            return []
        
        q = deque()
        q.append([root, 0]) # node, c
        #col_map[0: [root]]
        curr_row = 0
        while q:
            for i in range(len(q)):
                curr_node, curr_col = q.popleft()
                if curr_col < min_idx:
                    min_idx = curr_col
                if curr_col > max_idx:
                    max_idx = curr_col
                if (curr_row, curr_col) not in col_map:
                    col_map[(curr_row, curr_col)] = []
                col_map[(curr_row, curr_col)].append(curr_node.val)
                if curr_node.left:
                    q.append([curr_node.left, curr_col - 1])
                if curr_node.right:
                    q.append([curr_node.right, curr_col + 1])
            curr_row += 1
        res = []
        print(curr_row)
        print(col_map)
        print(min_idx, max_idx)
        for c in range(min_idx, max_idx + 1):
            res_tmp = []
            for r in range(curr_row):
                if (r, c) in col_map:
                    res_tmp.extend(sorted(col_map[r, c]))
            if len(res_tmp) > 0:
                res.append(res_tmp)
        
        
        return res
