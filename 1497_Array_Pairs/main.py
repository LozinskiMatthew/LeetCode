from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count = {}
        for num in arr:
            remainder = ((num % k) + k) % k
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

        for rem, count in remainder_count.items():
            if rem == 0:
                if count % 2 != 0:
                    return False
            else:
                complement = k - rem
                if complement not in remainder_count or remainder_count[complement] != count:
                    return False

        return True
