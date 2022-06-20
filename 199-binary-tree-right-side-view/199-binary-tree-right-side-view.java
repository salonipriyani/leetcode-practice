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
    public List<Integer> rightSideView(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        List<Integer> res = new ArrayList<>();
        if (root == null)
            return res;
        
        q.offer(root);
        while (!q.isEmpty()){
            int size = q.size();
            TreeNode rightside = null;
            for (int i = 0; i < size; i++){
                rightside = q.poll();
                if (rightside.left != null)
                    q.offer(rightside.left);
                if (rightside.right != null)
                    q.offer(rightside.right);
            }
            
            res.add(rightside.val);
        }
        return res;
    }
}