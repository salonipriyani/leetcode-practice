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
    public List<List<Integer>> levelOrder(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        
        q.add(root);
        List<List<Integer>> result= new ArrayList<>();
        if (root == null)
            return result;
        while(q.size() > 0){
            List<Integer> row = new ArrayList<>();
            int rowSize = q.size();
            while(rowSize > 0){
                TreeNode currentNode = q.remove();
                if(currentNode.left != null){
                    q.add(currentNode.left);
                }
                if(currentNode.right != null){
                    q.add(currentNode.right);
                }
                row.add(currentNode.val);
                rowSize--;
            }
            result.add(row);
        }
        return result;
    }
}