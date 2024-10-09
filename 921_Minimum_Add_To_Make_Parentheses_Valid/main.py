class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if len(s) == 0:
            return 0
        stack = []
        for par in s:
            if not stack:
                stack.append(par)
                continue
            if stack[-1] == "(" and par == ")":
                stack.pop()
            else:
                stack.append(par)
        return len(stack)

