class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s) - 1
        while r >= 0 and s[r] == " ":
            r -= 1
        counter = 0
        while r >= 0 and s[r] != " ":
            counter += 1
            r -= 1

        return counter