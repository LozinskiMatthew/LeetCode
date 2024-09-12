from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter = len(words)
        for word in words:
            for letter in word:
                if letter not in allowed:
                    counter -= 1
                    break
        return counter

if __name__ == "__main__":
    pass