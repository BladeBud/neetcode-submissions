class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        new_max = 0
    
        for number in nums:
            if number == 1:
                new_max += 1
                if new_max > max:
                    max = new_max
            else:
                new_max = 0
        return max
        