from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maximum = max(nums)
        max_counter = 0
        counter = 0
        for num in nums:
            if num == maximum:
                counter += 1
                if max_counter < counter:
                    max_counter = counter
            else:
                counter = 0
        return max_counter

if __name__ == "__main__":
    pass