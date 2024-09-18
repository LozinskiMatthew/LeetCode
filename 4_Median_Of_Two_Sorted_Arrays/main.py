from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1 = sorted(nums1)
        n = len(nums1)
        if n % 2 == 1:
            return nums1[n // 2]
        else:
            return (nums1[n // 2 - 1] + nums1[n // 2]) / 2.0

if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1, nums2))