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
    int diameter = 0;
    
    public int diameterOfBinaryTree(TreeNode root) {
        updateDiameter(root);
        return diameter;
    }
    
    public int updateDiameter(TreeNode node){
            if (node == null)
                return -1;
            int left = updateDiameter(node.left);
            int right = updateDiameter(node.right);

            diameter = Math.max(diameter, left + right + 2);

            return 1 + Math.max(left, right);
        }
}

