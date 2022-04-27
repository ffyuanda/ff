# https://leetcode.com/problems/3sum/

# This one is interesting, but not hard. It has the same gist
# as the 26-remove-duplicates-from-sorted-array: removing the duplicates

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for left in range(len(nums) - 2):
            
            # this step makes sure that we do not have any duplicates in our
            # result output 
            # it cannot be nums[left + 1], since that will rule out the whole
            # list of the same left values
            if left > 0 and nums[left] == nums[left - 1]:
                continue

            mid = left + 1
            right = len(nums) - 1

            while mid < right:

                curr_sum = nums[left] + nums[mid] + nums[right]

                if curr_sum < 0:
                    mid += 1

                elif curr_sum > 0:
                    right -= 1

                else:
                    result.append([nums[left], nums[mid], nums[right]])

                    # Avoiding duplicates check
                    while mid < right and nums[mid] == nums[mid + 1]:
                        mid += 1

                    # Avoiding duplicates check
                    while mid < right and nums[right] == nums[right - 1]:
                        right -= 1

                    mid += 1
                    right -= 1

        return result
