class Solution:
    def isValid(self, s: height) -> bool:
        left = ['{', '(', '[']
        right = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        stack = []

        for c in s:
            if c in left:
                stack.append(c)
            if c in right:
                if len(stack) > 0 and stack[-1] == right[c]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0