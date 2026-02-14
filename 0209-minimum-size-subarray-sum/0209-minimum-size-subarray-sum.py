class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ=0
        min_length=float('inf')
        left=0

        for right in range(len(nums)):
            summ +=nums[right]

            while summ >= target:
                min_length = min(min_length, right-left+1)
                summ -= nums[left]
                left+=1
        return 0 if min_length == float('inf') else min_length