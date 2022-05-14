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
    public void reorderList(ListNode head) {
        //split into 2 halves
        //reverse second
        //combine
        if (head == null || head.next == null)
            return;
        ListNode fast = head, slow = head, last = null;
        while(fast != null && fast.next != null){
            last = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        last.next = null;
        
        ListNode prev = null;
        while(slow != null){
            ListNode temp = slow.next;
            slow.next = prev;
            prev = slow;
            slow = temp;
        }
        
        ListNode l1 = head, l2 = prev;
        
        while(l1 != null){
            ListNode l1_next = l1.next;
            ListNode l2_next = l2.next;
            
            l1.next = l2;
            
            if(l1_next == null)
                break;
            
            l2.next = l1_next;
            l1 = l1_next;
            l2 = l2_next;
        }
        
       
    }
}