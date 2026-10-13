class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grup = {}
        for i in strs:
            sort_key = "".join(sorted(i))
            if sort_key not in grup:
                grup[sort_key] = []

            grup[sort_key].append(i)
        return list(grup.values())

        