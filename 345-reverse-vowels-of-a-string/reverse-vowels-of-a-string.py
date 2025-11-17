class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels_set = set("aeiouAEIOU")
        vowels = [c for c in s if c in vowels_set]
        res = []
        for c in s:
            if c in vowels_set:
                res.append(vowels.pop())
            else:
                res.append(c)
        return ''.join(res)
