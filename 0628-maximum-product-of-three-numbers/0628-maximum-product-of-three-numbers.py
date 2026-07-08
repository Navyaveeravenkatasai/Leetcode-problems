class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1

        prod1 = nums[right] * nums[right - 1] * nums[right - 2]

        prod2 = nums[left] * nums[left + 1] * nums[right]

        return max(prod1, prod2)