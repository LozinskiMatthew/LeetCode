class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x == 0:
            return 0
        x_stringed = str(x)
        if x_stringed[0] == "-":
            negative = True
            x_stringed = x_stringed[1:]
        x_stringed = x_stringed[::-1]
        x = int(x_stringed)
        if negative == True:
            x = -x
        cnt = 2**31
        if x < -cnt or x > cnt - 1:
            return 0
        else:
            return x