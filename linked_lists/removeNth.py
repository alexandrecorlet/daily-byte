# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Compute size of the list
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        if n == size:
            return head.next

        # Apply Runner technique
        i = 1
        prev = head
        curr = head.next
        while curr is not None and size - i != n:
            prev = prev.next        # move previous pointer
            curr = curr.next        # move curr pointer
            i += 1

        prev.next = curr.next
        return head
        
