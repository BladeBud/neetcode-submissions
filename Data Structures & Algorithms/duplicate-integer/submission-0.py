class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        b = set(nums)
        if len(b) == len(nums):
            return False
        else:
            return True
        