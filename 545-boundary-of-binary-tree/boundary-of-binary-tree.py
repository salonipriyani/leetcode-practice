# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def isLeaf(t):
            return t.left == None and t.right == None
        
        def addLeaves(res, node):
            if isLeaf(node):
                res.append(node.val)
            else:
                if node.left:
                    addLeaves(res, node.left)
                if node.right:
                    addLeaves(res, node.right)

        res = []
        if not root:
            return res
        
        if not isLeaf(root):
            res.append(root.val)
        
        t = root.left
        while t:
            if not isLeaf(t):
                res.append(t.val)
            if t.left != None:
                t = t.left
            else:
                t = t.right
        addLeaves(res, root)
        stack = []
        t = root.right
        while t:
            if not isLeaf(t):
                stack.append(t.val)
            if t.right:
                t = t.right
            else:
                t = t.left
        
        while stack:
            res.append(stack.pop())
        return res
