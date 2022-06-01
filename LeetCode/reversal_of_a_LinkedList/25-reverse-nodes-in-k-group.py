# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def remain_enough(head, k):
            
            while(head):
                head = head.next
                k -= 1
                if k == 0:
                    return True
            return False

        dummy = ListNode(val=0, next=head)
        prev = dummy
        curr = head
        
        while(remain_enough(curr, k)):
            for _ in range(k-1):
                temp = curr.next
                curr.next = temp.next
                temp.next = prev.next
                prev.next = temp
            prev = curr
            curr = curr.next
        return dummy.next
