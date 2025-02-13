# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        nullNodeFound = False

        q = deque()
        q.append(root)

        while q:
            curr = q.popleft()
            if nullNodeFound == False:
                if curr is None:
                    nullNodeFound = True
                else:
                    q.append(curr.left)
                    q.append(curr.right)
            else:
                if curr:
                    return False
        
        return True