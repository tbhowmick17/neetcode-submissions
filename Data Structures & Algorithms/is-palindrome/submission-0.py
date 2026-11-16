class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = (''.join(s.split())).lower()
        strs = ""
        for st in stripped:
            if st.isalnum():
                strs += st
        return strs == strs[::-1]