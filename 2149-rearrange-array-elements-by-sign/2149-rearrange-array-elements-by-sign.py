class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res1=[]
        res2=[]
        final=[]

        for i in range(len(nums)):
            if nums[i] > 0:
                res1.append(nums[i])
            else:
                res2.append(nums[i])
        n = len(nums)
        m=len(nums) // 2
        for i in range(n-m):
            final.append(res1[i])
            final.append(res2[i])
        return final