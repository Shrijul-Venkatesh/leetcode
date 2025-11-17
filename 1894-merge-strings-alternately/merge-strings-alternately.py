class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        while len(word1) > 0 and len(word2) > 0:
            res += word1[0] + word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
        res += word1 + word2

        return res