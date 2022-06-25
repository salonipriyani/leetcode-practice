/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int maxWidth;
    Map<Integer, Integer> leftmostPositions = new HashMap<>();
    public int widthOfBinaryTree(TreeNode root) {
        maxWidth = 0;
        dfs(root, 0, 0);
        return maxWidth;
    }
    
    public void dfs(TreeNode root, int depth, int position){
        if (root == null)
            return;
        if (!leftmostPositions.containsKey(depth))
            leftmostPositions.put(depth, position);
        maxWidth = Math.max(maxWidth, position - leftmostPositions.get(depth) + 1);
        dfs(root.left, depth+1, position*2);
        dfs(root.right, depth + 1, position * 2 + 1);
    }
}