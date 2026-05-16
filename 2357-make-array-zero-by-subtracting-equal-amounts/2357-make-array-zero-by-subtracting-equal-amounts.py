class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        nums = list(set(nums))
        count=0
        res=[]
        for ch in range(len(nums)):
            if nums[ch] > 0:
                res.append(nums[ch])
        return len(res)