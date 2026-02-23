from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        res = 0
        n = len(nums)
        for low in range(n):
            mid = low + 1
            while mid < n:
                if nums[mid] - nums[low] == diff:
                    high = mid + 1
                    while high < n:
                        if nums[high] - nums[mid] == diff:
                            res += 1
                        high += 1
                mid += 1
        return res