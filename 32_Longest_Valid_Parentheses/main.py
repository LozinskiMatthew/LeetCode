class Solution:
    def edit_length(self, max_len, curr_len):
        if max_len < curr_len:
            max_len = curr_len
        return max_len, 0

    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        curr_len = 0
        stack = []
        for char in s:
            if char == ")":
                if len(stack) == 0:
                    max_len, curr_len = self.edit_length(max_len, curr_len)
                else:
                    curr_len += 1
                    stack.pop()
            else:
                '''''
                if len(stack) == 1:
                    max_len, curr_len = self.edit_length(max_len, curr_len)
                    stack.append("(")
                    curr_len = 0
                else:
                    stack.append("(")
                '''''
                stack.append("(")
        max_len, curr_len = self.edit_length(max_len, curr_len)
        return max_len * 2

if __name__ == "__main__":
    solve = Solution()
    print(solve.longestValidParentheses("(()"))  # 2