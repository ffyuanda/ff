# https://leetcode.com/problems/circular-array-loop/

# A complex one, it is not triky, just complex, I
# don't think it will come up in an interview, cause it
# can easily kill the 50 minutes session ;-)


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        def get_next_index(nums, i):
            
            i += nums[i] % length
            if i < 0:
                i += length
            elif i > length - 1:
                i %= length
            return i

        length = len(nums)
        
        if not nums or length < 2:
            return False
        
        for i in range(length):
            
            if nums[i] == 0:
                continue
                
            slow = i
            fast = get_next_index(nums, slow)
            
            while nums[i] * nums[fast] > 0 and \
                  nums[i] * nums[get_next_index(nums, fast)] > 0:
                
                if slow == fast:
                    if slow == get_next_index(nums, slow):
                        break
                    return True
                
                slow = get_next_index(nums, slow)
                fast = get_next_index(nums, get_next_index(nums, fast))
            
            slow = i
            sgn = nums[i]
            
            while sgn * nums[slow] > 0:
                tmp = get_next_index(nums, slow)
                nums[slow] = 0
                slow = tmp
                
        return False
