class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        zeros=ones=0
        for i in range(0,n):
            if(nums[i]==0): zeros+=1
            if(nums[i]==1): ones+=1
        for i in range(0,zeros):
            nums[i]=0
        for i in range(zeros,zeros+ones):
            nums[i]=1
        for i in range(zeros+ones,n):
            nums[i]=2