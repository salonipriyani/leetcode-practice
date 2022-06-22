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
    int count = 0;
    List<Integer> arr = new ArrayList<>();
    public int pathSum(TreeNode root, int targetSum) {
        getSum(root, targetSum);
        return count;
    }
    
    public void getSum(TreeNode root, int sum){
        if (root == null)
            return;
        
        arr.add(root.val);
        getSum(root.left, sum);
        getSum(root.right, sum);
        int currSum = 0;
        for (int i = arr.size() - 1; i >= 0; i--){
            currSum += arr.get(i);
            if (currSum == sum)
                count++;
        }
        
        arr.remove(arr.size() - 1);
    }
    
}