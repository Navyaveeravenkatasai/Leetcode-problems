class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res=[]
        nums.sort()
        for ch in range(len(nums)):
           if  nums[ch] == target:
            res.append(ch)
        return res