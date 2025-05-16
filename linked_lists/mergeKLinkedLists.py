import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, [lists[i].val, i])
        
        merged = ListNode()
        curr = merged
        while heap:
            # pop from heap the min value
            val, i = heapq.heappop(heap)
            # merge
            curr.next = lists[i]
            curr = curr.next
            # go to the next value of the i-th linked list
            lists[i] = lists[i].next
            # If i-th linked list is not empty, then add the current value to the heap
            if lists[i]:
                heapq.heappush(heap, [lists[i].val, i])
        
        return merged.next

