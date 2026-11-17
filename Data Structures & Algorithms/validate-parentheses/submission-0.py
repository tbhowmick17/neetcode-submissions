class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        if s[0] in mapper.keys():
            return False

        stack = []
        for p in s:
            if p in "}])":
                if stack and stack[-1] == mapper[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)

        return stack == []


        
        