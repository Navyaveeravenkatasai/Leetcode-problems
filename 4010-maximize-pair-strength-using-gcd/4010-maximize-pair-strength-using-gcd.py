from math import gcd
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        maxi = 0
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                ans = ((nums[i] * nums[j]) // (gcd(nums[i], nums[j])) ** 2)
                maxi = max(ans, maxi)

        return maxi

