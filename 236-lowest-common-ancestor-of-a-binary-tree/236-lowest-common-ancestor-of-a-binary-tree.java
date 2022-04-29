/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    
    private TreeNode ans;
    
    public void Solution(){
        this.ans = null;
    }
    
    private boolean recurseTree(TreeNode currNode, TreeNode p, TreeNode q){
        if(currNode == null)
            return false;
        
        int left = this.recurseTree(currNode.left, p, q) ? 1 : 0;
        int right = this.recurseTree(currNode.right, p, q) ? 1 : 0;
        
        int mid = (currNode == p || currNode == q) ? 1 : 0;
        
        if(left + right + mid >= 2)
            this.ans = currNode;
        
        return (mid + left + right > 0);
    }
    
    
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        this.recurseTree(root, p, q);
        return this.ans;
    }
}