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
    public List<Double> averageOfLevels(TreeNode root) {
        
        List<Double> result = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        
        q.offer(root);
        double sum = 0;
        while(!q.isEmpty()){
            sum = 0;
            int size = q.size();
            for (int i = 0; i < size; i++){
                TreeNode currNode = q.poll();
                sum += currNode.val;
                if (currNode.left != null)
                    q.offer(currNode.left);
                if (currNode.right != null)
                    q.offer(currNode.right);
            }
            double avg = sum / size;
            
            result.add(avg);
        }
        
        return result;
    }
}