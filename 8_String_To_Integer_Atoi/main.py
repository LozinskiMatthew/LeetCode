class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        positive = True
        result = ""
        curr = s[0]
        while curr == " ":
            s = s[1:]
            if len(s) == 0:
                return 0
            curr = s[0]
        if len(s) == 0:
            return 0
        if s[0] == "-":
            positive = False
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        for thing in s:
            if thing.isdigit():
                result += thing
            else:
                break
        if result == "":
            return 0
        if int(result) == 0:
            return 0
        result = int(result)
        if positive == False:
            result = -result
        to_count = 2 ** 31
        if result > to_count - 1:
            return to_count - 1
        elif result < -to_count:
            return -to_count
        else:
            return result
