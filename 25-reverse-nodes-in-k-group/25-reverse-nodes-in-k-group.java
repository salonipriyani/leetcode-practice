/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummyHead = new ListNode(0, head);
        ListNode prevGroup = dummyHead;
        while (true){
            ListNode kth = getKth(prevGroup, k);
            if (kth == null)
                break;
            
            ListNode groupNext = kth.next;
            ListNode prev = kth.next;
            ListNode curr = prevGroup.next; 
            while (curr != groupNext){
                ListNode temp = curr.next;
                curr.next = prev;
                prev = curr;
                curr = temp;
            }
            ListNode temp = prevGroup.next;
            prevGroup.next = kth;
            prevGroup = temp;
        }
        
        return dummyHead.next;
    }
    
    public ListNode getKth(ListNode curr, int k){
        while (curr != null && k > 0){
            curr = curr.next;
            k--;
        }
        
        return curr;
    }
}