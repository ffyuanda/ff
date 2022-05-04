# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/middle-of-the-linked-list/

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            
            slow = slow.next
            fast = fast.next.next
        
        if fast.next:
            slow = slow.next
            
        return slow
