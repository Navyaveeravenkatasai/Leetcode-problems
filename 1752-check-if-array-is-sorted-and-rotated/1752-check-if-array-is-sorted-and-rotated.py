class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        for ch in range(len(nums)-1):
            if nums[ch] > nums[ch+1]:
                count += 1
        
        if nums[-1] > nums[0]:
            count += 1

        return count <= 1