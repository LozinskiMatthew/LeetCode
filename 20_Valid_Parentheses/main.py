class Solution:

    def isValid(self, s: str) -> bool:
        mapped = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if char in mapped:
                if len(stack) == 0 or mapped[char] != stack.pop():
                    return False

            else:
                stack.append(char)

        if len(stack) == 0:
            return True
        else:
            return False

if __name__ == "__main__":

    sol = Solution()
    # print(sol.isValid("()"))
    # print(sol.isValid("{()"))
    # print(sol.isValid("["))
    print(sol.isValid("([]()"))