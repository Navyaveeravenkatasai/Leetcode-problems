class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count=0
        for num in range(len(nums)):
            if nums[num] < k:
                count+=1
        return count