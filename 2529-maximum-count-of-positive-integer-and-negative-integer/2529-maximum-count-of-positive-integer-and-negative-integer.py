class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        n = len(nums)

        low = 0
        high = n

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > 0:
                high = mid
            else:
                low = mid + 1

        positive = n - low

        low = 0
        high = n

        while low < high:
            mid = (low + high) // 2

            if nums[mid] >= 0:
                high = mid
            else:
                low = mid + 1

        negative = low

        return max(positive, negative)