# https://leetcode.com/problems/linked-list-cycle-ii/

""" I did not come up with the solution myself, I referenced the Floyd cycle detection algorithm
(hare and tortoise algorithm) to solve the problem, a fast and a slow pointer. I will put the logic
behind the algorithm down below. """

""" Why it works: 
    set several variables:
    H = head node
    S = cycle's starting node
    M = first meet's meeting node
    X = the distance from H to S
    Y = the distance from S to M
    Z = the distance from M to S
    L = the length of the loop (from S to S)
    we have to prove that 'X mod L = Z'

    let's unravel the cycle and lay it out alongside the X distance thread
    we can observe that there can be K segments of L and a remainder distance R
    so X = K * L + R

    b/c X mod L = R

    and

    according to the algorithm, it basically says that R = Z

    so we are proving that X mod L = Z

    for the slow pointer, the distance it goes until the first meet is X + Y
    for the fast pointer, the distance it goes until the first meet is 2 * (X + Y) (two times faster)

    we can observe that:
        2 * (X + Y) = X + Y + K * L
        X + Y = K * L
        X = K * L - Y
        X mod L = L - Y
        X mod L = Z (prove done)
    """

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        slow, fast = head, head
        has_loop = False

        # check if there is a loop
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                fast = head
                has_loop = True
                break
                
        if not has_loop:
            return
                
        # find the starting node
        while fast is not slow:
            fast = fast.next
            slow = slow.next
            
        return fast
        