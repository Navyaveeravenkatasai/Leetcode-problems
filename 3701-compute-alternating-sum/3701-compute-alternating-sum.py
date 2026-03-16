class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
       num=0
       n=len(nums)
       for i in range(n):
            if i % 2 == 0:
                num+=nums[i]
            else:
                num-=nums[i]
       return num