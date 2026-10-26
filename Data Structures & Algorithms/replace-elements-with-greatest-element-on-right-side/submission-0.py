class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = -1
        i = len(arr) -1
        n = 0
        while  n <= i:
            x = arr[i]
            arr[i] = max
            if max < x:
                max = x
            i -= 1
        return arr