class Solution:
    def isPalindrome(self, s: str) -> bool:
        y = ""
        for x in s:
            if x.isalnum():
                y += x.lower()

        return y == y[::-1]