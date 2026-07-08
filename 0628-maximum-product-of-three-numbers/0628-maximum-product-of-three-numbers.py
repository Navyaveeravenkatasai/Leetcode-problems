class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1

        pro1 = nums[right] * nums[right-1] * nums[right-2]

        pro2 = nums[left] * nums[left+1] * nums[right]

        return max(pro1,pro2)