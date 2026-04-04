class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count=0
        left=[]
        right=[]
        for i in range(1,len(nums)):
            left=nums[:i]
            right=nums[i:]
            total=0

            total = sum(left) - sum(right)

            if abs(total) % 2 == 0:
                count += 1
        return count