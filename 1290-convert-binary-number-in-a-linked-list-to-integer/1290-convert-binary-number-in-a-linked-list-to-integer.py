# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        if head is None:
            return 0
        num = head.val
        while head.next:
            num = num * 2 + head.next.val
            head = head.next
            
        return num
            