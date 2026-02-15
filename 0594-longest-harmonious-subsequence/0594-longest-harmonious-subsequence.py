class Solution:
    def findLHS(self, nums: List[int]) -> int:
        left=0
        right=1
        res=0
        n=len(nums)
        nums.sort()
        while right < n:
            while nums[right] - nums[left]  > 1:
                left+=1
            if nums[right] - nums[left] == 1:
                res = max(res, right-left+1 )
            right+=1
        return res