# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        prev = None
        
        while head != None:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
            
        return prev