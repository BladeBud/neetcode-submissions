class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stripped = s.strip().split()
        return len(stripped[-1])
        