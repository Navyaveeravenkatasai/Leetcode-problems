class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = -1

        left = 0
        right = len(nums) - 1

        nums.sort()

        while left < right:

            if nums[left] == -nums[right]:
                res = max(res, nums[right])
                left += 1
                right -= 1

            elif abs(nums[left]) < abs(nums[right]):
                right -= 1

            else:
                left += 1

        return res