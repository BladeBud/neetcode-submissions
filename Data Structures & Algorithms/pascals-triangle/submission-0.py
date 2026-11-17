from math import comb

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        counts = []
        for n in range(numRows):
            row = [comb(n, k) for k in range(n + 1)]
            counts.append(row)
        return counts