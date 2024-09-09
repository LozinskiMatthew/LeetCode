class Solution:
    def edit_length(self, max_len, curr_len) -> int:
        if max_len < curr_len:
            max_len = curr_len
        return max_len

    def valid_len(self, s: str) -> int:
        stack = []
        for char in s:
            if char == ')':
                if len(stack) == 0:
                    return 0
                else:
                    stack.pop()
            else:
                stack.append(char)

        if len(stack) == 0:
            return len(s)
        else:
            return 0

    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        for i in range(0, len(s)):
            for j in range(i + 1, len(s) + 1):
                curr_len = self.valid_len(s[i:j])
                max_len = self.edit_length(max_len, curr_len)
        return max_len


if __name__ == "__main__":
    solve = Solution()
    print(solve.longestValidParentheses("()()"))  # 4, but prints 2










    '''
        def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        curr_len = 0
        iterr = 0
        stack = []

        if len(s) == 0:
            return 0

        while iterr < len(s):
            for i in range(iterr, len(s)):  # Iter cannot change
                char = s[i]
                if char == ")":
                    if len(stack) == 0:
                        max_len, curr_len = self.edit_length(max_len, curr_len)
                        iterr += 1
                        stack = []
                        break
                    else:
                        curr_len += 1
                        stack.pop()
                else:
                    stack.append("(")
            else:
                iterr = len(s)

            if iterr >= len(s):
                break

        max_len, curr_len = self.edit_length(max_len, curr_len)
        return max_len * 2
        # How to handle edge case in which I would have ()((), this should be 2 but is 4
    
    
    
    '''