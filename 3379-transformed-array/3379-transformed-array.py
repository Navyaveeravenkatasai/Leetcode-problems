class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res=[0] * len(nums)

        for i in range(len(nums)):
            index=(nums[i] + i) % len(nums)
            res[i] = nums[index]

        return res