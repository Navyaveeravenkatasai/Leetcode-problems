class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        freq={}
        n = len(nums)
        low = 0
        high = n

        mid = (low + high) // 2
        res = nums[mid]

        for ch in nums:
            freq[ch] =freq.get(ch,0) + 1

        if freq[res] > 1:
            return False
        return True
