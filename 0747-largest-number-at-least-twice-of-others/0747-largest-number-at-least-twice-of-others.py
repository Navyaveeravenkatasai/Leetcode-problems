class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        lar = max(nums)
        big = 0   
        for ch in range(0,len(nums)):
            if nums[ch] == lar:
                big = ch
            elif nums[ch] + nums[ch] <= lar:
                continue
            elif nums[ch] + nums[ch] > lar:
                return -1
        return big