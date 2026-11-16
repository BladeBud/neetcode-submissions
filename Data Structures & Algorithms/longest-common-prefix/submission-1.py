class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        shortest = min(strs, key=len)

        for i, char in enumerate(shortest):
            for word in strs:
                if word[i] != char:
                    return shortest[:i]
        return shortest