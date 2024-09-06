class Solution:
    # ))) (
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        curr_len = 0
        stack = []
        n = False
        for char in s:
            if char == ")":
                if len(stack) != 0:
                    top_element = stack.pop()
                else:

                elif:

                else:
                n = False

        else:
            stack.append(char)
