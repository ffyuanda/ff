# https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        if len(nums) >= k:
            for i in range(k):
                heapq.heappush(self.nums, nums[i])
            for i in range(k, len(nums)):
                heapq.heappushpop(self.nums, nums[i])
        else:
            for i in range(len(nums)):
                heapq.heappush(self.nums, nums[i])

    def add(self, val: int) -> int:
        if len(self.nums) == self.k:
            heapq.heappushpop(self.nums, val)
        else:
            heapq.heappush(self.nums, val)
            
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
