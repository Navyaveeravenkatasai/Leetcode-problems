from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)

        # If exactly 3 elements, sum all
        if n == 3:
            return sum(nums)

        minimum = nums[n - 1]
        res = float('inf')

        for i in range(n - 2, 0, -1):
            res = min(res, nums[i] + minimum)
            minimum = min(minimum, nums[i])

        return res + nums[0]
