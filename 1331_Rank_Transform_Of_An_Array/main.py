class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_uniq = sorted(set(arr))

        hashed = {val: i + 1 for i, val in enumerate(arr_uniq)}

        return [hashed[i] for i in arr]