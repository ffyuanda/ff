# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        
        # normal fast & slow pointers
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        node = None
        
        # reverse it from slow
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
            
        # approach from both sides            
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
# Definition for singly-linked list.
# https://leetcode.com/problems/palindrome-linked-list/

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        
        # normal fast & slow pointers
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        node = None
        
        # reverse it from slow
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
            
        # approach from both sides            
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
