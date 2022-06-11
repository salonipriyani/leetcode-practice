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
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null)
            return head;
        
        int len = 1;
        ListNode tail = head;
        while(tail.next != null){
            len++;
            tail = tail.next;
        }
        k = k % len;
        if (k == 0)
            return head;
        ListNode cur = head;
        for(int i = 0; i < len - k - 1; i++){
            cur = cur.next;
        }
        ListNode newHead = cur.next;
        cur.next = null;
        
        tail.next = head;
        
        return newHead;
    }
}