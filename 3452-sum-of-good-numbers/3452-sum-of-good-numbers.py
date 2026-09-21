class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)

        for i in range(n):
            if i - k >= 0 and nums[i] <= nums[i-k]:
                continue
            if i + k <= n - 1 and nums[i] <= nums[i+k]:
                continue
            res += nums[i]

        return res