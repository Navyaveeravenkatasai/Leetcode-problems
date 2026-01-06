class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        return nums[n-1] - nums[n-2]
        if len(n) <2:
            return 0