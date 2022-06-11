/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        Queue<Node> q = new LinkedList<>();
        if (root == null)
            return root;
        q.offer(root);
        while (!q.isEmpty()){
            int size = q.size();
            for (int i = 0; i < size; i++){
                Node currNode = q.poll();
                if (currNode.right != null){
                    currNode.left.next = currNode.right;
                    if (currNode.next != null)
                        currNode.right.next = currNode.next.left;
                }
                if (currNode.left != null)
                    q.offer(currNode.left);
                if(currNode.right != null)
                    q.offer(currNode.right);
            }
        }
        return root;
    }
}