class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sumi = 0
        for num in range(len(nums)):
            sumi += nums[num]
        return sumi % k
