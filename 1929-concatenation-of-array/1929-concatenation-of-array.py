class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        rev_array=nums[::-1]
        nums=nums+nums
        return nums