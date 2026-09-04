class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        for i in range(n):
            maxi_res = nums[:i + 1]
            mini_res = nums[i:]

            maxi = max(maxi_res)
            mini = min(mini_res)

            sumi = maxi - mini

            if sumi <= k:
                return i

        return -1