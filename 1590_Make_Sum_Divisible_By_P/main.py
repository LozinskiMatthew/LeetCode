from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)

        if total_sum % p == 0:
            return 0

        remainder = total_sum % p
        rm = {0: -1}
        cp = 0
        min_len = len(nums)

        for i, num in enumerate(nums):
            cp = (cp + num) % p
            target = (cp - remainder) % p

            if target in rm:
                sub_len = i - rm[target]
                min_len = min(min_len, sub_len)

            rm[cp] = i

        return min_len if min_len < len(nums) else -1
