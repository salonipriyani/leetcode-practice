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
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) 
            return head;
        ListNode[] arr = partition(head);
        ListNode l1 = sortList(arr[0]);
        ListNode l2 = sortList(arr[1]);
        return mergeTwo(l1, l2);
    }
    
    private ListNode[] partition(ListNode head){
        ListNode slow = head, fast = head, last = null;
        while (fast != null && fast.next != null){
            last = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        
        last.next = null;
        return new ListNode[]{head, slow};
    }
    
    private ListNode mergeTwo(ListNode l1, ListNode l2){
        ListNode dummyHead = new ListNode();
        ListNode currNode = dummyHead;
        while (l1 != null && l2 != null){
            if (l1.val < l2.val){
                currNode.next = l1;
                l1 = l1.next;
            }
            else{
                currNode.next = l2;
                l2 = l2.next;
            }
            currNode = currNode.next;
        }
        
        if (l1 != null){
            currNode.next = l1;
            l1 = l1.next;
            currNode = currNode.next;
        } else{
            currNode.next = l2;
            l2 = l2.next;
            currNode = currNode.next;
        }
        
        return dummyHead.next;
    }
}