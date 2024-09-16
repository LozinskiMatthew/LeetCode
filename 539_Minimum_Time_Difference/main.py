from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        low_result = 720
        lowest_result = 720
        for i in range(len(timePoints)):
            for j in range(len(timePoints)):
                if i == j:
                    continue
                low_result = abs(60 * int(timePoints[i][:2]) + int(timePoints[i][3:5]) - (60 * int(timePoints[j][:2]) + int(timePoints[j][3:5])))
                if low_result == 0:
                    return 0
                if low_result > 720:
                    low_result = 720 - (low_result - 720)
                if low_result < lowest_result:
                    lowest_result = low_result
        return lowest_result

if __name__ == "__main__":
    i = "23:59"
    j = "00:00"
    table = ["00:00","23:59","00:00"]
    table2 = [i, j]
    low_result = abs(60 * int(i[:2]) + int(i[3:5]) - (60 * int(j[:2]) + int(j[3:5])))
    if low_result > 720:
        low_result = 720 - (low_result - 720)
    # print(low_result)

    print(Solution().findMinDifference(table2))