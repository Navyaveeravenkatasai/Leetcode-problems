class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res=[]
        nums.sort()
        m=nums[0]
        n=nums[len(nums)-1]
        for ch in range(m,n+1):
                if ch not in nums:
                    res.append(ch)
        return res