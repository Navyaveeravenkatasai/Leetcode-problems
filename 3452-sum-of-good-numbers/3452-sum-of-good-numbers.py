class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            if (i-k < 0 or nums[i] > nums[i-k]) and \
               (i+k >= len(nums) or nums[i] > nums[i+k]):
                count += nums[i]

        return count