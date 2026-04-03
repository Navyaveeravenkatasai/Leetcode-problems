class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        n=len(nums)
        target=[]
        for num in range(n):
            target.insert(index[num],nums[num])
        return target
            