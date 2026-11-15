class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        alphabets = [0] * 26

        for i in range(len(s)):
            ord_s = ord(s[i]) - ord('a')
            ord_t = ord(t[i]) - ord('a')

            alphabets[ord_s] += 1
            alphabets[ord_t] -= 1

        for count in alphabets:
            if count != 0:
                return False
        
        return True
