# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#https://leetcode.com/problems/linked-list-cycle-ii
# https://leetcode.com/problems/linked-list-cycle-ii/discuss/44781/Concise-O(n)-solution-by-using-C%2B%2B-with-Detailed-Alogrithm-Description

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        fast = head
        slow = head
        entry = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
                        
            if fast == slow:
                while slow != entry:
                    slow = slow.next
                    entry = entry.next
                
                return entry
            
        return None
