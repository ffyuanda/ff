# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        curr = head
        _next = None

        while curr.next:
            prev = curr.next
            curr.next = _next
            _next = curr
            curr = prev
            
        curr.next = _next
        return curr
