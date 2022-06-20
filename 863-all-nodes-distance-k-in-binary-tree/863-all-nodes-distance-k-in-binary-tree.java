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
    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        List<Integer> ans = new ArrayList<>();
        Map<TreeNode, TreeNode> parentsMap = new HashMap<>();
        buildParentMap(root, root, parentsMap);
        Set<TreeNode> visited = new HashSet<>();
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(target);
        visited.add(target);
        int level = 0;
        while(!q.isEmpty()){
            int size = q.size();
            if (level == k)
                return buildListFromQueue(q);
            for (int i = 0; i < size; i++){
                TreeNode currNode = q.poll();
                if (currNode.left != null && !visited.contains(currNode.left)){
                    q.offer(currNode.left);
                    visited.add(currNode.left);
                }
                
                if (currNode.right != null && !visited.contains(currNode.right)){
                    q.offer(currNode.right);
                    visited.add(currNode.right);
                }
                
                TreeNode parent = parentsMap.get(currNode);
                if (!visited.contains(parent)){
                    q.offer(parent);
                    visited.add(parent);
                }
            }
            level++;
        }
        return ans;
    }
    
    public void buildParentMap(TreeNode root, TreeNode parent, Map<TreeNode, TreeNode> parentsMap){
        if (root == null)
            return;
        parentsMap.put(root, parent);
        buildParentMap(root.left, root, parentsMap);
        buildParentMap(root.right, root, parentsMap);
    }
    
    public List<Integer> buildListFromQueue(Queue<TreeNode> q){
        List<Integer> ls = new ArrayList<>();
        while(!q.isEmpty()){
            ls.add(q.poll().val);
        }
        
        return ls;
    }
}