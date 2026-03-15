from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        left = 0
        max_len = 1

        for right in range(1, len(nums)):
            
            if nums[right] <= nums[right-1]:
                left = right     
            
            max_len = max(max_len, right - left + 1)

        return max_len