class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []

        for i in range(n):
                nums.append(start)
                start += 2

        res = 0

        for ch in nums:
            res ^= ch

        return res
