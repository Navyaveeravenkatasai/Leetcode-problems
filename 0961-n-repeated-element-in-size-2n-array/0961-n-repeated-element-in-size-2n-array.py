class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        freq={}
        count=0
        for ch in nums:
            freq[ch] = freq.get(ch,0) + 1
        
        n = len(nums)/2

        for value in freq:
            if freq[value] == n:
                return value
            