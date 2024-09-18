from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted(nums, reverse=True)
        return nums[k-1]



if __name__ == "__main__":
    nums = [4, 3, 6, 8, 5, 7, 9, 0]
    sol = Solution()
    print(sol.findKthLargest(nums, 3))