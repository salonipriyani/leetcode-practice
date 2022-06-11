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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode dummyHead = new ListNode(0, head);
        ListNode p = dummyHead, c = head;
        
        for (int i = 0; i < left - 1; i++){
            p = p.next;
            c = c.next;
        }
        
        int i = 0;
        ListNode prev = null;
        while(i < right - left + 1){
            ListNode temp = c.next;
            c.next = prev;
            prev = c;
            c = temp;
            i++;
        }
        
        p.next.next = c;
        p.next = prev;
        
        return dummyHead.next;
    }
}