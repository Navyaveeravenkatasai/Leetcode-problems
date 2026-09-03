class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        res = 0
        sumi = 0
        max_range = 0
        for ch in nums:
            maxi = float('-inf') 
            mini = float('inf')
            for digit in str(ch):
                maxi = max(int(digit),maxi)
                mini = min(int(digit),mini)
            sumi = maxi - mini
            if sumi > max_range:
                max_range = sumi
                res = ch
            elif sumi == max_range:
                res += ch
        return res