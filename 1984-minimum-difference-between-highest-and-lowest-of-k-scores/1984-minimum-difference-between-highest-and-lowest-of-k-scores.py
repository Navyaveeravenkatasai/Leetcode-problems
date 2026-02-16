class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        nums.sort()
        n=len(nums)
        left=0
        res=float('inf')
        for right in range(n):
            if right - left + 1 == k:
                diff = nums[right] - nums[left]
                res=min(res,diff)
                left+=1
        return res  
