class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        maxi=0
        if len(nums) <2:
            return maxi
        nums.sort()
        for i in range(1,len(nums)):
            temp=nums[i] - nums[i-1]
            if temp>maxi:
                maxi=temp
        return maxi