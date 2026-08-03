class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        res=[]
        even=odd=0

        for i in reversed(nums):
            if i % 2 == 0:
                even += 1
                res.append(odd)
            else:
                odd += 1
                res.append(even)

        return res[::-1]