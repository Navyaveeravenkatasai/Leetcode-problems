class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        first = 0
        double = 0
        for ch in range(len(nums)):
            if nums[ch] < 10:
                first += nums[ch]
            else:
                double += nums[ch]

        return first != double