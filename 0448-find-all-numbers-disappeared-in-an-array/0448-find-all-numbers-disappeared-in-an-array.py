class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans=[0] * (n+1)
        res=[]
        for i in range(n):
            ans[nums[i]] = 1
        for i in range(1,n+1):
            if ans[i] == 0:
                res.append(i)
        return res