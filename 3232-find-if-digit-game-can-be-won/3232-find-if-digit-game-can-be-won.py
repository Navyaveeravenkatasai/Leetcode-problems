class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        first = 0
        for ch in range(len(nums)):
            if nums[ch] < 10:
                first += nums[ch]
        second = 0

        for ch in range(len(nums)):
            if nums[ch] >= 10:
                second += nums[ch]

        if first > second or second > first:
            return True
        return False