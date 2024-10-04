from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        hashed = {}
        result = 0
        k = (sum(skill) / len(skill)) * 2
        for ski in skill:
            if ski not in hashed:
                hashed[ski] = 1
            else:
                hashed[ski] += 1
        for ski in skill:
            diff = k - ski
            if diff not in hashed:
                return -1
            else:
                if hashed[diff] == 1:
                    hashed.pop(k - ski, None)
                else:
                    hashed[diff] -= 1
                result += ski * (diff)
        return int(result / 2)


