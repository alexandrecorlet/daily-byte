# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle singleton and empty list
        if not head or not head.next:
            return head
        
        prev = head
        curr = head.next
        while curr:
            temp = curr.next        # save next node
            curr.next = prev        # set next node to be the previous (reverse reference)
            prev = curr             # advance previous node to current
            curr = temp             # advance current node to next
        head.next = None
        return prev
