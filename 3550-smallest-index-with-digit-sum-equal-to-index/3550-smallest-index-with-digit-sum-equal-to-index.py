class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        res= []

        for ch in range(len(nums)):
            if sum(int(digit) for digit in str(nums[ch])) == ch:
                res.append(ch)
        
        if len(res) == 0:
            return -1
        else:
            return res[0]