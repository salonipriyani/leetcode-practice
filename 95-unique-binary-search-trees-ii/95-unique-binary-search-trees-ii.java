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
    public List<TreeNode> generateTrees(int n) {
        return findNumTrees(1, n);
    }
    private List<TreeNode> findNumTrees(int start, int end){
        List<TreeNode> res = new ArrayList<>();
        if (start > end){
            res.add(null);
            return res;
        }
        
        for (int i = start; i<= end; i++){
            List<TreeNode> leftTrees = findNumTrees(start, i - 1);
            List<TreeNode> rightTrees = findNumTrees(i+1, end);
            for (TreeNode leftTree: leftTrees){
                for (TreeNode rightTree: rightTrees){
                    TreeNode newRoot = new TreeNode(i);
                    newRoot.left = leftTree;
                    newRoot.right = rightTree;
                    res.add(newRoot);
                }
            }
        }
        return res;
    }
}