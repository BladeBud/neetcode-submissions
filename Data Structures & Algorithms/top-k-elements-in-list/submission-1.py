from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        buc = [[] for i in range(len(nums) + 1)]
        for num, freq in count.items():
            buc[freq].append(num)

        res = []
        for freq in range(len(buc) - 1, 0 , -1):
            for num in buc[freq]:
                res.append(num)
                if len(res) == k:
                    return res