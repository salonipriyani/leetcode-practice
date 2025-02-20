# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        leftToRight = True
        res= []
        level_list = deque()
        while q:
            curr_level = deque()
            n = len(q)
            for i in range(n):
                curr = q.popleft()
                if leftToRight:
                    curr_level.append(curr.val)
                else:
                    curr_level.appendleft(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(list(curr_level))
            leftToRight = not leftToRight
        return res