# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge2lists(l1, l2):
            dummyhead = curr = ListNode(0)
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            if not l1:
                curr.next = l2
            if not l2:
                curr.next = l1
            return dummyhead.next

        tot = len(lists)
        interval = 1
        while interval < tot:
            for i in range(0, tot - interval, interval * 2):
                lists[i] = merge2lists(lists[i], lists[i + interval])
            
            interval *= 2
        return lists[0] if tot > 0 else None