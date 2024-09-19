from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        midrow = len(matrix) // 2

        if min(matrix[midrow]) <= target <= max(matrix[midrow]):
            for i in matrix[midrow]:
                if i == target:
                    return True
            return False
        else:
            if target < min(matrix[midrow]):
                return self.searchMatrix(matrix[:midrow], target)
            else:
                return self.searchMatrix(matrix[midrow + 1:], target)