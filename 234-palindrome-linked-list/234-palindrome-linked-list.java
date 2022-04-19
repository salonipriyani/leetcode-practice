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
    public boolean isPalindrome(ListNode head) {
        /* 2 pointers: fast and slow
        bring slow to middle
        slow = slow.next;
        make previous next null - cut from the middle
        reverse second half
        iterate through both LLs and check if equal */
        
        ListNode fast = head, slow = head, prev;
        
        while(fast !=  null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        prev = slow;
        slow = slow.next;
        prev.next = null;
        
        while(slow != null){
            ListNode temp = slow.next;
            slow.next = prev;
            prev = slow;
            slow = temp;
        }
        fast = head;
        slow = prev;
        while (slow != null){
            if (slow.val != fast.val)
                return false;
            
            slow = slow.next;
            fast = fast.next;
        }
        
        return true;
    }
}