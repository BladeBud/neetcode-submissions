class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i in maps:
                top = stack.pop() if stack else "#"
                if maps[i] != top:
                    return False
            else:
                stack.append(i)
        return not stack