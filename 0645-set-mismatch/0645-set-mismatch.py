class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)

        duplicate = -1
        missing = -1

        for ch in range(1,n+1):
            res.append(ch)

        for num in nums:
            if nums.count(num) == 2:
                duplicate = num
                break

        for num in res:
            if num not in nums:
                missing = num
                break

        return [duplicate,missing]