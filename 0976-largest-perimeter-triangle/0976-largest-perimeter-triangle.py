class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for ch in range(len(nums)-3,-1,-1):
            if nums[ch] + nums[ch+1] > nums[ch+2]:
                return nums[ch] + nums[ch+1] + nums[ch+2]
        return 0
