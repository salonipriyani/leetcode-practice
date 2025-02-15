# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.idx = -1
        self.sorted_tree = []
        self.in_order(self.root)
    
    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        self.sorted_tree.append(root.val)
        self.in_order(root.right)


    def next(self) -> int:
        if self.idx + 1 < len(self.sorted_tree):
            self.idx += 1
            return self.sorted_tree[self.idx]

    def hasNext(self) -> bool:
        if self.idx + 1 < len(self.sorted_tree):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()