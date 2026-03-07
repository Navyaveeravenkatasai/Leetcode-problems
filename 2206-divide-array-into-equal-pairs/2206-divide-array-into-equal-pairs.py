
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = {}

        for ch in nums:
            freq[ch] = freq.get(ch, 0) + 1

        for i in freq.values():
            if i % 2 != 0:   # if any frequency is odd
                return False

        return True