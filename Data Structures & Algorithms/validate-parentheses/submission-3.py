class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in mapping.values():  # opening bracket
                stack.append(ch)
            else:  # closing bracket
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()

        return not stack