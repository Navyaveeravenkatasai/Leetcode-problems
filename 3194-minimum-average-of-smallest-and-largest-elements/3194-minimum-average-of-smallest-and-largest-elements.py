class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        res=[]
        avg=0
        nums.sort()
        left=0
        right=len(nums)-1

        while left < right:
            avg = (nums[left] + nums[right]) / 2
            res.append(avg)
            left+=1
            right-=1
        return min(res)

