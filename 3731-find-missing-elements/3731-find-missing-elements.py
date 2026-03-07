class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res=[]
        m=min(nums)
        n=max(nums)
        for ch in range(m,n+1):
                if ch not in nums:
                    res.append(ch)
        return res