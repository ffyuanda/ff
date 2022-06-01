# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return None
        
        nodes = []        
        dummy = ListNode(val=0, next=head)
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        nodes = collections.deque(nodes)
        k %= len(nodes)
                
        while k:
            c = nodes.pop()
            
            c.next = dummy.next
            dummy.next = c
            nodes.appendleft(c)
            
            nodes[-1].next = None
            k -= 1
        
        return dummy.next
