from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        mid = int(len(nums) / 2)
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            return self.searchInsert(nums[:mid], target)
        if target > nums[mid]:
            return mid + 1 + self.searchInsert(nums[mid + 1:], target)