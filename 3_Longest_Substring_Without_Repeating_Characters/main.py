class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        k = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        if len(s) == 2:
            if s[0] == s[1]:
                return 1
            else:
                return 2
        for i in range(len(s)):
            temp_set = set()
            for k in range(i, len(s)):
                if s[k] in temp_set:
                    break
                else:
                    temp_set.add(s[k])
            if longest < len(temp_set):
                longest = len(temp_set)
        return longest