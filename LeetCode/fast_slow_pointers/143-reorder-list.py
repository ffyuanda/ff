# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # important method
        def reverse_list(head):
            nxt = None
            
            while head:
                prev = head.next
                head.next = nxt
                nxt = head
                head = prev

            return nxt
            
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        reversed_head = reverse_list(slow)
        head1, head2 = head, reversed_head
        
        while head1 and head2:
            nxt1 = head1.next
            nxt2 = head2.next

            head1.next = head2
            head1 = nxt1

            head2.next = head1
            head2 = nxt2
