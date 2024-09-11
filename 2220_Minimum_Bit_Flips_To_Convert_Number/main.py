class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        answer = 0
        goal = str(bin(goal)[2:])
        start = str(bin(start)[2:])
        diff = len(start) - len(goal)
        diff_abs = abs(diff)
        if diff < 0:
            start = diff_abs * "0" + start
        elif diff > 0:
            goal = diff_abs * "0" + goal
        for num in range(len(start)):
            if start[num] != goal[num]:
                answer += 1
        return answer



if __name__ == "__main__":
    goal = 4
    goal = bin(goal)
    goal = goal[2:]
    goal = str(goal)
    print(goal)