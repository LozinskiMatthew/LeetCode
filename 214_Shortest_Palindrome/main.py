class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        if s == s[::-1]:
            return s
        rev_s = s[::-1]
        for i in range(len(s)):
            if s.startswith(rev_s[i:]):
                return rev_s[:i] + s

if __name__ == '__main__':
    s = "aacecaaa"
    solution = Solution()
    print(solution.shortestPalindrome(s))