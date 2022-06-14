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
    public int maxDepth(TreeNode root) {
        if (root == null)
            return 0;
        Stack<TreeNode> st = new Stack<>();
        st.push(root);
        Stack<Integer> val = new Stack<>();
        val.push(1);
        int max = 0;
        while (!st.isEmpty()){
            TreeNode temp = st.pop();
            int tempVal = val.pop();
            
            if (temp.left == null && temp.right == null)
                max = Math.max(max, tempVal);
            
            if(temp.left != null){
                st.push(temp.left);
                val.push(tempVal + 1);
            }
            if(temp.right != null){
                st.push(temp.right);
                val.push(tempVal + 1);
            }
        }
        
        return max;
    }
}