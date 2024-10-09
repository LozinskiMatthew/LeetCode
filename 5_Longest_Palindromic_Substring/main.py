class Solution:
    def isLonger(self, result: str, current: str) -> str:
        if len(current) > len(result):
            return current
        else:
            return result

    def isPalindrome(self, string: str) -> bool:
        if string == string[::-1]:
            return True
        else:
            return False

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        result = ""
        for l in range(n):
            for r in range(l + 1, n + 1):
                if self.isPalindrome(s[l:r]):
                    result = self.isLonger(result, s[l:r])

        return result
