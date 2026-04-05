class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        temp = nums
        max1=max(temp)
        temp.remove(max1)
        max2=max(temp)
        return ((max1-1) * (max2 - 1))