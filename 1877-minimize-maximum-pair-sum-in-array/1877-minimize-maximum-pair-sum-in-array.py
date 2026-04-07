class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        res=[]
        while left < right:
            sum = nums[left] + nums[right]
            res.append(sum)
            left+=1
            right-=1
        return max(res)

        