from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(x) for x in nums]
        def compare(a, b):
            if int(a+b) > int(b+a):
                return -1
            else:
                return 1
        nums = sorted(nums, key=cmp_to_key(compare))
        if nums[0] == "0":
            return "0"
        return "".join(nums)

if __name__ == "__main__":
    nums = [3,30,34,5,9]
    sol = Solution()
    print(sol.largestNumber(nums))