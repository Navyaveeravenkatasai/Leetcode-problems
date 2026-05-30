class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        for ch in range(len(nums) - 1):

            if nums[ch] % 2 == nums[ch + 1] % 2:
                return False

        return True