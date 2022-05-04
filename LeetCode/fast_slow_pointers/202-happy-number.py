# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum
        
        slow_runner = n
        fast_runner = n
        
        while True:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
            if slow_runner == fast_runner or fast_runner == 1:
                break
        return fast_runner == 1
