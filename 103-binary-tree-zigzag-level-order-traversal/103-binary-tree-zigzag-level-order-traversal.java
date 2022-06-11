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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null)
            return res;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        boolean odd = true;
        while(!q.isEmpty()){
            int size = q.size();
            List<Integer> subList = new ArrayList<>();
            for (int i = 0; i < size; i++){
                TreeNode currNode = q.poll();
                if(odd)
                    subList.add(currNode.val);
                else
                    subList.add(0, currNode.val);
                if (currNode.left != null)
                    q.offer(currNode.left);
                if (currNode.right != null)
                    q.offer(currNode.right);
            }
            res.add(subList);
            odd = !odd;
        }
        
        return res;
    }
}