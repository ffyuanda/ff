# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if left == right:
            return head
        
        dummyNode = ListNode()
        dummyNode.next = head
        cur, prev = head, dummyNode
        
        for _ in range(left - 1):
            cur = cur.next
            prev = prev.next
        
        # normal iterative reverse
        # this is super elegant, refer to the drawing .92.png
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp
        
        return dummyNode.next
