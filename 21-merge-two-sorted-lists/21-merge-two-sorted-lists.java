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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode merge = new ListNode(0), l1 = list1, l2 = list2;
        ListNode mergeHead = merge;
        while(l1 != null && l2 != null){
            if(l1.val <= l2.val){
                merge.next = l1;
                l1 = l1.next;
            }
            else{
                merge.next = l2;
                l2 = l2.next;
            }
            merge = merge.next;
        }
        
        while(l1 != null){
            merge.next = l1;
            merge = merge.next;
            l1 = l1.next;
        }
        
        while(l2 != null){
            merge.next = l2;
            merge = merge.next;
            l2 = l2.next;
        }
        
        return mergeHead.next;
        
    }
}