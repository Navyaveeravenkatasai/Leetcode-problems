class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count=0
        freq={}

        for ch in nums:
            freq[ch] = freq.get(ch,0) + 1


        for key in freq:
            if freq[key] == 1:
                count+=key
        return count
