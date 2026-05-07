class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if original not in nums:
            return original
        total=0
        res=[]
        while original in nums:
            if original in nums:
                original = original * 2

        return original