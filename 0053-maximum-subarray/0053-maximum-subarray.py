class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total=0
        maxi=float("-inf")
        n=len(nums)

        for i in range(n):
            total=total+nums[i]
            maxi=max(maxi,total)

            if(total<0):
                total=0
        return maxi