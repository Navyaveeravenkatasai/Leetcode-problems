class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        total=1
        maxi=float("-inf")
        n=len(nums)
        for i in range (0,n):
            total=nums[i]
            for j in range(i+1,n):
                total=total*nums[j]
                maxi=max(total,maxi)
        return maxi