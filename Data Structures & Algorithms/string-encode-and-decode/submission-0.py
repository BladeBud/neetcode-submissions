class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)

        while i < n:
            j = s.find("#", i)
            leng = int(s[i:j])
            st = j + 1
            res.append(s[st : st+ leng])
            i = st + leng
        return res
