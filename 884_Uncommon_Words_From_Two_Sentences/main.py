from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s3 = s1 + " " + s2 + " "
        k = 0
        words = []
        for letter in range(len(s3)):
            if s3[letter] == " ":
                words.append(s3[k:letter])
                k = letter + 1
        element_counts = {x: words.count(x) for x in words}
        words = [x for x in words if element_counts[x] == 1]
        return words

if __name__ == "__main__":
    s1 = "this apple is sweet"
    s2 = "this apple is sour"
    print(Solution().uncommonFromSentences(s1, s2))