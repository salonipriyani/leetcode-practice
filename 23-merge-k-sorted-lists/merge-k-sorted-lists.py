# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        counter = 0
        for l in lists:
            if l:
                heapq.heappush(heap, [l.val, counter, l])
                counter += 1

        dummy = ListNode(0)
        curr = dummy
        while heap:
            heap_val, count, heap_node = heapq.heappop(heap)
            curr.next = heap_node
            curr = curr.next
            if heap_node.next:
                heapq.heappush(heap, [heap_node.next.val, counter, heap_node.next])
                counter += 1
        return dummy.next
